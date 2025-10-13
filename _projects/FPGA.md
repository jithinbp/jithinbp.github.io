---
layout: project
title: 'FPGA SLG47910'
date: 13 Oct 2025
image: 
  path: /assets/img/blog/shrike.jpeg
caption: Fiddling with the Shrike Lite from Vicharak

twitter:
  image: /assets/img/blog/shrike.jpeg
  card: summary_large_image

description: >
  Just getting started..
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

![](/assets/img/blog/shrike_blink_fpga.webp)

I'm on Ubuntu 22

* got micropython-mpremote, thonny installed via Synaptic
* cd test
* opened Thonny, and Tools-Options-Interpreter = RP2040 Micropython (Or check the bottom right corner)
* Tested blinky. test/blink_rp2040.py 

## Uploading bitstream

Open thonny, and view-files. Now right click on the .bin bitstream and copy to the RP2040

![](/assets/img/blog/shrike_copy.png)

In the RP_2040 terminal (This is micropython on the RP2040 now. not your system interpreter), upload the .bin to the FPGA. Don't forget to verify the filename :p

![](/assets/img/blog/shrike_flash.png)


## Now I need the FPGA toolchain from [Renesas](https://www.renesas.com/en/products/slg47910/part-details/slg47910v)