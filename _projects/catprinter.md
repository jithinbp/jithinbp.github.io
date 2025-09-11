---
layout: project
title: 'Reverse engineering thermal printer'
date: 1 Feb 2024
image: 
  path: /assets/img/blog/catprinter.webp
caption: Reverse engineering thermal printer
description: >
  So i bought this cute cat thermal printer for 1000 Rs, hoping to reverse engineer it and and run
  it from a python script over bluetooth.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

## Reverse engineering thermal printer

![](/assets/img/thumbs/catprint.jpg) So i bought this cute cat thermal printer for 1000 Rs, hoping to reverse engineer it and and run
it from a python script over bluetooth.

while waiting for it to deliver, I found several other reverse engineering efforts, and it seemed
like I had my job cut out for me..  however, none of the 4 blogs i followed worked for the model I
got. The tutorial on apk decompilation by [Werwolv](https://werwolv.net/blog/cat_printer) was quite detailed
so I set out to decompile the app that works with my printer. perhaps i can get it working with some minorcommand
tweaks.

##  Downloaded the apk 
Press the power button twice, and it gives you a scan code to download a 180 MB apk. but the same app 
can be found on the play store as `fun print` , and the same developer `yintibao` has another app called iBleem
which also works with this printer.

## Decompilation

[http://www.javadecompilers.com/apk](http://www.javadecompilers.com/apk)

uploaded the massive 180MB apk, and received a 207MB zip file within a minute. takes up 450 MB when unzipped. 
This app could be a few MB if you didn't need so many bells and whistles.


## bluetoothctl

```c
[MXW01:/service0008/char0016]# gatt.
gatt.acquire-notify             gatt.register-service
gatt.acquire-write              gatt.release-notify
gatt.attribute-info             gatt.release-write
gatt.clone                      gatt.select-attribute
gatt.list-attributes            gatt.unregister-application
gatt.notify                     gatt.unregister-characteristic
gatt.read                       gatt.unregister-descriptor
gatt.register-application       gatt.unregister-includes
gatt.register-characteristic    gatt.unregister-service
gatt.register-descriptor        gatt.write
gatt.register-includes          
[MXW01:/service0008/char0016]# gatt.list-attributes 
Primary Service (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0040
	0000ae3a-0000-1000-8000-00805f9b34fb
	Unknown
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0040/char0043
	0000ae3c-0000-1000-8000-00805f9b34fb
	Unknown
Descriptor (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0040/char0043/desc0045
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0040/char0041
	0000ae3b-0000-1000-8000-00805f9b34fb
	Unknown
Primary Service (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008
	0000ae30-0000-1000-8000-00805f9b34fb
	Unknown
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0016
	0000ae10-0000-1000-8000-00805f9b34fb
	Unknown
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0013
	0000ae05-0000-1000-8000-00805f9b34fb
	Unknown
Descriptor (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0013/desc0015
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0010
	0000ae04-0000-1000-8000-00805f9b34fb
	Unknown
Descriptor (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0010/desc0012
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char000e
	0000ae03-0000-1000-8000-00805f9b34fb
	Unknown
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char000b
	0000ae02-0000-1000-8000-00805f9b34fb
	Unknown
Descriptor (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char000b/desc000d
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0008/char0009
	0000ae01-0000-1000-8000-00805f9b34fb
	Unknown
Primary Service (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0004
	00001801-0000-1000-8000-00805f9b34fb
	Generic Attribute Profile
Characteristic (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0004/char0005
	00002a05-0000-1000-8000-00805f9b34fb
	Service Changed
Descriptor (Handle 0x0000)
	/org/bluez/hci0/dev_48_0F_57_11_2D_EE/service0004/char0005/desc0007
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[MXW01:/service0008/char0016]# 

```


## Trying Bluetooth HCI snoop log

enabled it from developer options


adb bugreport anewbugreportfolder


## Receive

on characteristic 0xAE02 , received following on eDebugger android app when lid opened/closed

------------------------------------o/c-----------
22 21 A1 03 0A 00 00 00 00 49 1B 00 01 01 2F 07 00
22 21 A1 03 0A 00 00 00 00 49 1B 00 00 00 42 07 00

got this with simplepyble library when the lid wasopened.
22 21 a1 03 0a 00 00 00 00 49 1c 00 01 01 2d 0b 00


no dice so far...



##


```
public void openNotification() {
    BleManager.getInstance().notify(
        this.connectingDevice,
        this.charactristicNotiy.getService().getUuid().toString(), 
        this.charactristicNotiy.getUuid().toString(),
        new BleNotifyCallback() {
            public void onCharacteristicChanged(byte[] data) {
                // This is where AE02 notifications are received
                if (data.length != 0) {
                    // Process incoming data
                    String firstByte = byteToHex(data[0]);
                    if ("01".equals(firstByte)) {
                        // Handle flow control response
                        new Thread() {
                            public void run() {
                                synchronized (flowLock) {
                                    FlowWriteForV10G.setGredit(
                                        Integer.parseInt(byteToHex(data[1]), 16)
                                    );
                                    FlowWriteForV10G.setCanWriteFlag(true);
                                    flowLock.notify();
                                }
                            }
                        }.start();
                    }
                }
            }
            // ... other callback methods
        }
    );
}
```

The notification handler is set up when the device is connected and services are discovered. The code listens for incoming data on the notification characteristic (AE02) and processes it, particularly for flow control responses where:

+ It checks the first byte of the response
+ If the first byte is "01", it handles flow control by:
  + Setting the credit value from the second byte
  + Enabling the write flag
  + Notifying the flow control lock

This is part of the flow control mechanism where the printer uses AE02 to tell the app when it's ready to receive more data via AE01.
