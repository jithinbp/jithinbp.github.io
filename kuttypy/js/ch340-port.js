/**
 * CH340/CH341 USB-serial port for Android Chrome (WebUSB).
 * Implements the subset of Web Serial SerialPort used by KuttyPyDevice.
 * Ported from Linux ch341.c + selevo/WebUsbSerialTerminal (Apache/MIT references).
 */

const REQ_WRITE_REG = 0x9a;
const REQ_READ_REG = 0x95;
const REQ_SERIAL_INIT = 0xa1;
const REQ_MODEM_CTRL = 0xa4;

const REG_BAUD_FACTOR = 0x1312;
const REG_BAUD_OFFSET = 0x0f2c;
const REG_CONTROL_STATUS = 0x2727;

/** Precomputed CH340 baud divisors (Linux driver / WCH tables). */
const BAUD_TABLE = {
  600: { factor: 0x6481, offset: 0x76 },
  1200: { factor: 0xb281, offset: 0x3b },
  2400: { factor: 0xd981, offset: 0x1e },
  4800: { factor: 0x6482, offset: 0x0f },
  9600: { factor: 0xb282, offset: 0x08 },
  14400: { factor: 0xd980, offset: 0xeb },
  19200: { factor: 0xd982, offset: 0x07 },
  38400: { factor: 0x6483, offset: 0 },
  57600: { factor: 0x9883, offset: 0 },
  115200: { factor: 0xcc83, offset: 0 },
};

const MODEM_ON = 0xdf;
const MODEM_OFF = 0xff;

function emptyDataView() {
  return new DataView(new ArrayBuffer(0));
}

class UsbInSource {
  constructor(device, endpoint, onError) {
    this.type = 'bytes';
    this.device = device;
    this.endpoint = endpoint;
    this.onError = onError;
  }

  pull(controller) {
    (async () => {
      try {
        const size = this.endpoint.packetSize || 32;
        const result = await this.device.transferIn(this.endpoint.endpointNumber, size);
        if (result.status !== 'ok') {
          controller.error(`USB read: ${result.status}`);
          this.onError();
          return;
        }
        if (result.data?.buffer) {
          const chunk = new Uint8Array(
            result.data.buffer,
            result.data.byteOffset,
            result.data.byteLength,
          );
          controller.enqueue(chunk);
        }
      } catch (err) {
        controller.error(String(err));
        this.onError();
      }
    })();
  }
}

class UsbOutSink {
  constructor(device, endpoint, onError) {
    this.device = device;
    this.endpoint = endpoint;
    this.onError = onError;
  }

  async write(chunk, controller) {
    try {
      const result = await this.device.transferOut(this.endpoint.endpointNumber, chunk);
      if (result.status !== 'ok') {
        controller.error(result.status);
        this.onError();
      }
    } catch (err) {
      controller.error(String(err));
      this.onError();
    }
  }
}

export class Ch340SerialPort {
  constructor(usbDevice) {
    this._device = usbDevice;
    this._interfaceNumber = null;
    this._inEndpoint = null;
    this._outEndpoint = null;
    this._readable = null;
    this._writable = null;
    this._opened = false;
    this._modemOn = false;
  }

  getInfo() {
    return {
      usbVendorId: this._device.vendorId,
      usbProductId: this._device.productId,
    };
  }

  get readable() {
    return this._readable;
  }

  get writable() {
    return this._writable;
  }

  async open(options) {
    const baudRate = options?.baudRate ?? 9600;
    await this._device.open();
    if (this._device.configuration === null) {
      await this._device.selectConfiguration(1);
    }

    const iface = this._findVendorInterface();
    this._interfaceNumber = iface.interfaceNumber;
    const alt = iface.alternates[0];
    for (const ep of alt.endpoints) {
      if (ep.type === 'bulk' && ep.direction === 'in') this._inEndpoint = ep;
      if (ep.type === 'bulk' && ep.direction === 'out') this._outEndpoint = ep;
    }
    if (!this._inEndpoint || !this._outEndpoint) {
      throw new Error('CH340 bulk endpoints not found');
    }

    await this._device.claimInterface(this._interfaceNumber);
    await this._device.selectAlternateInterface(this._interfaceNumber, 0);
    await this._initChip(baudRate);

    this._opened = true;
    this._readable = new ReadableStream(new UsbInSource(
      this._device,
      this._inEndpoint,
      () => { this._readable = null; },
    ));
    this._writable = new WritableStream(new UsbOutSink(
      this._device,
      this._outEndpoint,
      () => { this._writable = null; },
    ));
  }

  async close() {
    if (this._readable) {
      try { await this._readable.cancel(); } catch (_) { /* ignore */ }
    }
    if (this._writable) {
      try { await this._writable.abort(); } catch (_) { /* ignore */ }
    }
    this._readable = null;
    this._writable = null;

    if (this._opened) {
      try {
        await this._modemCtrl(MODEM_OFF);
      } catch (_) { /* ignore */ }
    }

    if (this._device.opened) {
      try {
        if (this._interfaceNumber !== null) {
          await this._device.releaseInterface(this._interfaceNumber);
        }
      } catch (_) { /* ignore */ }
      await this._device.close();
    }
    this._opened = false;
  }

  async setSignals(signals) {
    if (!this._opened) return;
    if (signals.dataTerminalReady === false && signals.requestToSend === false) {
      await this._modemCtrl(MODEM_OFF);
      this._modemOn = false;
    } else if (signals.dataTerminalReady === true || signals.requestToSend === true) {
      await this._modemCtrl(MODEM_ON);
      this._modemOn = true;
    }
  }

  _findVendorInterface() {
    const configuration = this._device.configurations[0];
    for (const iface of configuration.interfaces) {
      const alt = iface.alternates[0];
      if (alt.interfaceClass === 0xff) {
        return iface;
      }
    }
    throw new Error('CH340 vendor interface (0xFF) not found');
  }

  async _vendorOut(request, value, index = 0, data = emptyDataView()) {
    const result = await this._device.controlTransferOut({
      requestType: 'vendor',
      recipient: 'device',
      request,
      value,
      index,
    }, data);
    if (result.status !== 'ok') {
      throw new Error(`CH340 control out failed: ${result.status}`);
    }
  }

  async _vendorIn(request, value, length, index = 0) {
    const result = await this._device.controlTransferIn({
      requestType: 'vendor',
      recipient: 'device',
      request,
      value,
      index,
    }, length);
    if (result.status !== 'ok') {
      throw new Error(`CH340 control in failed: ${result.status}`);
    }
    return result.data;
  }

  async _setBaudRate(baudRate) {
    const entry = BAUD_TABLE[baudRate];
    if (!entry) {
      throw new Error(`CH340: unsupported baud rate ${baudRate}`);
    }
    const empty = emptyDataView();
    await this._vendorOut(REQ_WRITE_REG, REG_BAUD_FACTOR, entry.factor, empty);
    if (entry.offset) {
      await this._vendorOut(REQ_WRITE_REG, REG_BAUD_OFFSET, entry.offset, empty);
    }
    await this._vendorOut(REQ_WRITE_REG, REG_CONTROL_STATUS, 0, empty);
  }

  async _modemCtrl(value) {
    await this._vendorOut(REQ_MODEM_CTRL, value, 0, emptyDataView());
  }

  async _initChip(baudRate) {
    const empty = emptyDataView();
    await this._vendorOut(REQ_SERIAL_INIT, 0xc29c, 0xb2b9, empty);
    await this._modemCtrl(MODEM_ON);
    await this._modemCtrl(0x9f);

    let status = await this._vendorIn(REQ_READ_REG, 0x0706, 2);
    if (status && status.getInt16(0, true) < 0) {
      throw new Error('CH340 status read failed during init');
    }

    await this._vendorOut(REQ_WRITE_REG, REG_CONTROL_STATUS, 0, empty);
    await this._setBaudRate(baudRate);

    status = await this._vendorIn(REQ_READ_REG, 0x0706, 2);
    if (status && status.getInt16(0, true) < 0) {
      throw new Error('CH340 status read failed after baud set');
    }
    await this._vendorOut(REQ_WRITE_REG, REG_CONTROL_STATUS, 0, empty);
    await this._modemCtrl(MODEM_ON);
    this._modemOn = true;
  }
}
