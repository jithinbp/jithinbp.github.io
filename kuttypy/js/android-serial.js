/**
 * Android Chrome serial access via WebUSB (desktop keeps native Web Serial).
 */

import { isAndroidChrome } from './platform.js';
import { Ch340SerialPort } from './ch340-port.js';
import { SerialPort as CdcSerialPort } from '../vendor/web-serial-polyfill.js';

const CH340_VENDOR = 0x1a86;
const MCP2200_VENDOR = 0x04d8;

export { isAndroidChrome } from './platform.js';

function toUsbFilters(serialFilters) {
  return serialFilters.map((f) => ({
    vendorId: f.usbVendorId,
    productId: f.usbProductId,
  }));
}

/**
 * Request a KuttyPy serial port. Desktop uses Web Serial; Android uses WebUSB
 * with a CH340-specific driver or the CDC polyfill for MCP2200.
 * @param {SerialPortFilter[]} serialFilters
 * @returns {Promise<SerialPort>}
 */
export async function requestKuttyPyPort(serialFilters) {
  if (!isAndroidChrome()) {
    if (!('serial' in navigator)) {
      throw new Error('Web Serial API is not available. Use Chrome or Edge.');
    }
    return navigator.serial.requestPort({ filters: serialFilters });
  }

  if (!('usb' in navigator)) {
    throw new Error(
      'WebUSB is not available on this Android browser. Use Chrome with USB OTG.',
    );
  }

  const device = await navigator.usb.requestDevice({ filters: toUsbFilters(serialFilters) });

  if (device.vendorId === CH340_VENDOR) {
    return new Ch340SerialPort(device);
  }
  if (device.vendorId === MCP2200_VENDOR) {
    return new CdcSerialPort(device);
  }

  throw new Error(
    `Unsupported USB device 0x${device.vendorId.toString(16)}:0x${device.productId.toString(16)}`,
  );
}
