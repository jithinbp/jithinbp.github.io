---
layout: project
title: 'Web Based Graphical coding'
date: 20 Jan 2013
image:  
  path: /assets/img/hobby/dd1.jpg
links:
  - title: Youtube
    url: https://www.youtube.com/watch?v=
caption: Drag and drop graphical programming in jquery. long before I was introduced to Scratch and Blockly
description: >
    Readings acquired from an instrument are being plotted in real time
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#40182a 0%,#3d1d3c 30%,#e700ff 50%,#9900e9 70%,#008729 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}


![](/assets/img/hobby/dd2.png)
Simple text based configuration file can be used to generate a graphical control screen. The mnemonics need to be mapped to the corresponding GPIB addresses on linux-gpib running on the server. Adding an optional 'display' argument activates a display field in the GUI
{:.figcaption}


![](/assets/img/hobby/dd3.png)
JQuery-UI based widgets can be dragged around and repositioned. Interconnects can be made by dragging labels and dropping them on targets. The GUI also enables a real-time camera feed.
{:.figcaption}

![](/assets/img/hobby/dd4.png)
Plotting a Parabola. A simple demonstration on how to use the loops and variables to plot a parabola
{:.figcaption}


This web based application allows users to quickly set up data acquisition rigs on a web-browser that remotely interfaces with scientific instruments connected to the web server.

I wrote the backend on Python which uses CherryPy to host webpages as well as real-time data from instruments.  OpenCV is used to read the data stream from a webcam, and Python-gpib (a wrapper for linux-gpib) interfaces with GPIB dongles.

The Jquery-AJAX based frontend serves as a primitive programming interface. I’ve included support for variables as well as a few loops.  Plotting is carried out using flot.jquery. This was how I started out with JQuery, and JS in general, and a lot of good open-source platforms for webapps have emerged since. therefore, this project stands abandoned.
