---
layout: project
title: 'Bacterial Growth Profile Monitor'
date: Feb 2025
image: 
  path: /assets/img/blog/turcover.jpeg
caption: A small wireless turbidity meter
description: >
  Developed for a student project, this meter has an LED and a linear light sensor to monitor the growth of bateria in an innoculated medium. An ESP32 relays the luminosity measurements to my server via MQTT
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

## Bacterial Growth Profile Monitor

The designs were made in FreeCAD, and I used a Bambulabs P1S to print them. The dual design is to simultaneously monitor a control and an innoculated medium.

![](/assets/img/blog/tur1.png)

![](/assets/img/blog/tur2.png)

## Results

growth of e-coli at 25C . all phases can be seen

![](/assets/img/blog/turplot.png)

## Automatic cell plate reader

Repurposed a benchtop CNC as a cell plate reader using Python and GCode

![](/assets/img/blog/autocell.webp){:.lead}


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">For every elegant solution, there exists a trashy amateur solution 😌<br>CNC mill controlled via gcode to visit each cell and measure luminosity with a TSL2591. The mirror and LED is a bad hack till I get a backlight. <br>Placed in a black box while measuring over 2 days. <a href="https://t.co/VENd6xGLIa">https://t.co/VENd6xGLIa</a> <a href="https://t.co/2s2DrKR6vJ">pic.twitter.com/2s2DrKR6vJ</a></p>&mdash; Jithin B.P., Ph.D. (@jithinbp_) <a href="https://twitter.com/jithinbp_/status/1927988604758020422?ref_src=twsrc%5Etfw">May 29, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 