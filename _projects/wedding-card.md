---
layout: project
title: 'Wedding Card'
date: 20 Oct 2024
image:  
  path: /assets/img/card/card.webp
screenshot: /assets/img/blog/card.webp
links:
  - title: Youtube
    url: https://www.youtube.com/watch?v=
  - title: Instructions
    url: https://www.hackster.io/jithinbp/ch32v003-blinky-wedding-card-fc8f60
  - title: Github
    url: https://github.com/jithinbp/ch32v003-card
  - title: Webpage
    url: /wedding
caption: My Wedding card based on a cheap risc-v CH32V003 IC
description: >
    Low cost wedding invites with a cheap RISC-V microcontroller that has LED POV display, RGB, IR receiver, Li-Ion and charger via USB-C !<br>
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#40182a 0%,#3d1d3c 30%,#e700ff 50%,#9900e9 70%,#008729 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}


I needed a super affordable BoM to make an electronic wedding invite. Thanks to a couple of open source projects, and CNLohrs work on the Library, the CH32V003 became a good option.

Schematics originally based on [Christmas LED ball](https://www.hackster.io/fabiosouza/christmas-ornament-based-on-ch32v003-riscv-mcu-2793db){:target="_blank"} .

Full schematics and firmware is available on my github page.

![](/assets/img/card/card_collage.jpg)

## PERSISTENCE OF VISION DISPLAY

![](/assets/img/card/card.avif)

![](/assets/img/card/card1.avif)


## Features

* USB C 6 pin connector with TP4057 for charging : 2 LEDs show charging status
* 3.7V battery : Li-ION chosen because the CR2032 (non rechargeable) only go up to 3V, and drop below 2.7 quite easily causing the WS2812-2020 RGB LED to glitch.
* CH32V003 processor : F4P6 variant. easy for hand soldered prototypes.
* 14 LEDs : 0805 SMD LEDs, Pink , Yellow , and White
* 1 RGB LED ; WS2812
* IR Receiver : TSOP38238
* Reed switch for timing the POV display ; replace with an Axxelerometer at the earliest
* footprints for BMP280 ( not tested yet )

## Software features

* RGB LED control
* PWM fading of LEDs : controls the MOSFET to adjust brightness of all LEDs together
* IR receiver via interrupt : removed from the final version. I'll bring it back later after I add an IR transmitter. Planning to make some interactive games with this.
* Interrupt wake up and deep sleep.
* Persistence of vision display using 8 LEDs

![](/assets/img/card/card2.avif)


## Credits

* Fábio Souza for the CH32v003 layout for the LED christmas ball which served as a starting point for this work.
* [CNLohr] (https://github.com/cnlohr/) for the many examples on ch32v003fun from where I lifted sections for H/W interrupts (for IR), deep sleep mode and wakeup, and PWM. The datasheet was also of much help. :)

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My <a href="https://twitter.com/hashtag/CH32V003?src=hash&amp;ref_src=twsrc%5Etfw">#CH32V003</a> dev board is up and running!<br>✅ Lots of blinkies 🚨 <br>✅ WS2812b-2020<br>✅ IR TX/RX<br>✅ Li-ion charger , type C 🔋 <br>✅ Deep sleep, interrupts, and POV display ✨ <a href="https://twitter.com/hackadayio?ref_src=twsrc%5Etfw">@hackadayio</a> <a href="https://twitter.com/cnlohr?ref_src=twsrc%5Etfw">@cnlohr</a> <a href="https://twitter.com/FabioSouza_io?ref_src=twsrc%5Etfw">@FabioSouza_io</a> <a href="https://twitter.com/aggarwal_pallav?ref_src=twsrc%5Etfw">@aggarwal_pallav</a> <a href="https://twitter.com/m_akshai?ref_src=twsrc%5Etfw">@m_akshai</a> <a href="https://twitter.com/MakeAugusta?ref_src=twsrc%5Etfw">@MakeAugusta</a> <a href="https://t.co/4kMVrwAMC4">pic.twitter.com/4kMVrwAMC4</a></p>&mdash; Jithin B.P., Ph.D. (@jithinbp_) <a href="https://twitter.com/jithinbp_/status/1800898778003890442?ref_src=twsrc%5Etfw">June 12, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
