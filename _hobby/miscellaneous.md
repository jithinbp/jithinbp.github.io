---
layout: project
title: 'Miscellaneous Projects'
date: 20 Jan 2012
image:  
  path: /assets/img/hobby/misc_cover.jpg
links:
  - title: Youtube
    url: https://www.youtube.com/watch?v=
caption: Random things I built in my dorm
description: >
    dismantled, old CRT monitor pretends to be an oscilloscope, a birthday card with optic fibers etc
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#40182a 0%,#3d1d3c 30%,#e700ff 50%,#9900e9 70%,#008729 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}


## Dismantled, old CRT monitor pretends to be an oscilloscope

I happened to have an old monitor that needed to be thrown out, so why not take it apart and see how it works.

A little research indicated that two deflection coils were present for either axis, and while one was a sawtooth waveform at around 35KHz, the other swept in the vertical direction at a modest 60Hz. If no input signal is applied, these two ensure that the electron beam scans the entire screen 60 times per second.


![](/assets/img/hobby/monitor.jpg)
The monitor with the plastic case removed
{:.figcaption}


Poking around the electronics (Careful! High voltages meant for the electron gun! ) , I located the wires to each of these deflection coils, and obtained confirmation by momentarily disconnecting either of them and observing the beam trace a straight line instead of scanning the entire screen.


![](/assets/img/hobby/monitor2.jpg)
With the X-axis deflection coil disconnected, the beam can now only scan along the vertical direction
{:.figcaption}

![](/assets/img/hobby/rgb.jpg)
The field from the oblong magnet taped on the screen changes the path of the scanning electron beam and deflects it into adjacent Red, Green, or Blue pixels, thereby causing brilliant patterns to form.
{:.figcaption}

![](/assets/img/hobby/monitor_sine.jpg)
I have now replaced the X-axis coil’s input (35KHz) with a 24Volts, 50Hz sinusoidal source from a step down transformer.
The vertical coil continues to scan at sawtooth 60Hz, and this results in an almost complete waveform being formed on the screen.
With some added analog electronics, and a variable frequency sawtooth source for the time axis, a primitive analog oscilloscope can be designed.
{:.figcaption}


## DIY greeting card with variable lighting effects

RGB LEDs with built in ICs that gradually change hue are widely available.
Add them as backlights to a greeting card with stained glass paintings made on transparency sheets, and a bunch of optic fibers(with scratches to induce light leaks at favourable points) , and you’ve got a greeting card with a nice touch. :)
Consumer grade optical fibers made from plastic can be easily sourced from showpieces .
The photograph doesn’t really show the details well, but you could try it out yourself.

![](/assets/img/hobby/cropped-birthday-card-normal.jpg)

![](/assets/img/hobby/cropped-birthday-card-nightmode-1.jpg)
