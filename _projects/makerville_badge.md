---
layout: project
title: 'The Makerville Badge'
date: 24 Sep 2025
image: 
  path: /assets/img/projects/makerville_badge.webp
caption: Implement visual coding on this badge!
description: >
  Winging it.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}

![](/assets/img/blog/mv3.jpeg)

Made an API endpoint to set RGB color

```c
void handleRGB(AsyncWebServerRequest *request)
{
  Serial.println("request on /rgb");
  String R = request->arg("R");
  String G = request->arg("G");
  String B = request->arg("B");
  pixel.setPixelColor(0, pixel.Color(R.toInt(), G.toInt(), B.toInt())); // Set to green
  pixel.show();                                                         // Set pixel
  request->send(200, "text/plain", "OK");
}

server.on("/rgb", HTTP_GET, handleRGB);

```

## The Makerville ESP32 Badge

### Mutliplication tables

Made an API endpoint to update text

![](/assets/img/projects/makerville_badge_table.webp)

```c
void handleSetText(AsyncWebServerRequest *request)
{
  if (request->hasArg("text"))
  {
    String textArg = request->arg("text");
    displayText = textArg;
  }
  request->send(200, "text/plain", "OK");
}

void scrollOn(AsyncWebServerRequest *request)
{
  scrolling = true;
  request->send(200, "text/plain", "OK");
}

  server.on("/text", HTTP_GET, handleSetText);
  server.on("/scrollOn", HTTP_GET, scrollOn);
  server.on("/scrollOff", HTTP_GET, scrollOff);

```

### Objectives

* test BLE
* Set text on the OLED with the existing firmware
* host a web server running visual programming on this, and make a wifi endpoint to set badge text.



## Simple Python app to scan BLE

```python
# ble_scanner.py
# pip install bleak
import asyncio
from bleak import BleakScanner

async def scan_ble_devices():
    """
    Scans for Bluetooth Low Energy devices and prints their details.
    """
    try:
        devices = await BleakScanner.discover(timeout=5.0)

        if not devices:
            print("No BLE devices found.")
            return
        print(f"\nFound {len(devices)} device(s):\n")
        # Iterate through and print
        for i, device in enumerate(devices, 1):
            print(f"--- Device {i} ---")
            if hasattr(device,'address'):print(f"  Address: {device.address}")
            if hasattr(device,'name'):print(f"  name: {device.name}")
            if hasattr(device,'rssi'):print(f"  rssi: {device.rssi} dBm")
            if hasattr(device,'metadata'):print(f"  Meta: {device.metadata}")
            print("-" * 20)

    except Exception as e:
        print(f"An error occurred: {e} \n  permissions?")

if __name__ == "__main__":
    asyncio.run(scan_ble_devices())
```

outputs

```bash
jithin@jithin-Victus:~/Downloads/tmp/makerville$ python3 test.py 
Starting BLE scan... (Press Ctrl+C to stop)
Scanning may take a few seconds.

Found 5 device(s):
~~~
--- Device 3 ---
  Address: DC:06:75:39:FF:6C
  name: Makerville Badge
--------------------
```


So the MAC is DC:06:75:39:FF:6C . Now to send data.

Can't do that. Issues with BLE on my Ubuntu running on HP Victus. 
Using an Android app called BLE Tester

![](/assets/img/blog/mv1.jpeg)

### It Works!

![](/assets/img/blog/mv2.jpeg)


## Setting up Platform-io

