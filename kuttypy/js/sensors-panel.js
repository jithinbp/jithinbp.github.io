/**
 * I2C sensors panel — scan, ID probe, detected sensor tiles.
 */

import { createSensorDriver } from './sensors.js';
import { identifyDetectedSensors, sensorMeta } from './sensor-probe.js';
import { openSensorDialog } from './sensor-dialog.js';

export function initSensorsPanel(root, device, {
  setStatus,
  isConnected,
  withPollingPaused,
  stopPolling,
  startPolling,
}) {
  const btnScan = root.querySelector('.btn-i2c-scan');
  const buttonsEl = root.querySelector('.sensor-buttons');
  let openDialog = null;

  function clearButtons() {
    buttonsEl.innerHTML = '';
  }

  function renderSensorButtons(detected) {
    clearButtons();
    if (!detected.length) {
      buttonsEl.innerHTML = '<p class="sensor-buttons-empty">No supported sensors identified</p>';
      return;
    }

    for (const { typeId, address } of detected) {
      const meta = sensorMeta(typeId);
      if (!meta) continue;

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'sensor-chip';
      btn.title = `${meta.name} @ 0x${address.toString(16).toUpperCase()}`;
      btn.innerHTML = `
        <img class="sensor-chip-icon" src="images/icons/${meta.icon}" alt="">
        <span class="sensor-chip-name">${meta.name}</span>
        <span class="sensor-chip-addr">0x${address.toString(16).toUpperCase().padStart(2, '0')}</span>
      `;
      btn.addEventListener('click', () => openSensor(typeId, address));
      buttonsEl.appendChild(btn);
    }
  }

  function openSensor(typeId, address) {
    if (!isConnected()) {
      setStatus('Connect device to open sensor');
      return;
    }
    openDialog?.close?.();
    const driver = createSensorDriver(typeId, device, address);
    if (!driver) return;

    openDialog = openSensorDialog({
      typeId,
      address,
      driver,
      withPollingPaused,
      stopPolling,
      startPolling,
      isConnected,
    });
  }

  async function scan() {
    if (!isConnected()) {
      setStatus('Connect device to scan I2C bus');
      return;
    }
    btnScan.disabled = true;
    btnScan.textContent = 'Scanning…';
    clearButtons();
    buttonsEl.innerHTML = '<p class="sensor-buttons-empty">Identifying sensors…</p>';
    try {
      const detected = await withPollingPaused(async () => {
        const addrs = await device.i2cScan();
        if (!addrs.length) return { addrs, sensors: [] };
        const sensors = await identifyDetectedSensors(device, addrs);
        return { addrs, sensors };
      });

      if (detected.addrs.length) {
        btnScan.textContent = detected.addrs
          .map((a) => '0x' + a.toString(16).toUpperCase().padStart(2, '0'))
          .join(' ');
        renderSensorButtons(detected.sensors);
        if (!detected.sensors.length) {
          setStatus('I2C devices found but no supported sensor IDs matched');
        }
      } else {
        btnScan.textContent = 'No devices';
        clearButtons();
      }
    } catch (err) {
      btnScan.textContent = 'Scan failed';
      clearButtons();
      setStatus(err.message);
    } finally {
      btnScan.disabled = !isConnected();
    }
  }

  btnScan.addEventListener('click', scan);

  return {
    setConnected(connected) {
      btnScan.disabled = !connected;
      if (!connected) {
        btnScan.textContent = 'I2C Scan';
        clearButtons();
        openDialog?.close?.();
        openDialog = null;
      }
    },
    reset() {
      btnScan.textContent = 'I2C Scan';
      clearButtons();
    },
  };
}
