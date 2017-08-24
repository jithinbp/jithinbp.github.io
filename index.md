---
layout: default
title: Google Summer of Code 2017
description: "Student : Jithin B.P &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mentor : FOSSASIA"
---

## Project Abstract : Develop firmware and experiments for Pocket Science Lab (PSLab)
---

Characteristic of a shift into the digital era, students have started to learn to code at an early age. However, most of the academic applications are currently centered around purely software based learning techniques such as simulations.

The ability to easily access multiple control and measurement tools as well as analyze the results from one common platform (such as is common in advanced research labs ) enables students to design new experiments and further the spirit of science.

The Pocket Science lab is such a platform precisely, and its architecture makes it an affordable tool for the masses, that has the potential to nurture young scientists.

### Mentors : Lorenz Gerber, Kiwi, Praveen Patil (Gnovi), Greg Austic, Ansgar Schmidt, Darwin Gosal, Wan Leung Wong, Ajithkumar bp, Mitch Altman, Shams Jaber, Victoria Bondarchuk, Mario Behling, Haggen So, Soong Chee Gi

## Work Completed
* * *

For GSoC-17, I worked on several aspects of the [Pocket Science Lab](pslab.fossasia.org) Project:

* [Firmware development of the PSLab](https://github.com/fossasia/pslab-firmware) : Code for PIC24E processor written with MPLab IDE and compiled with XC16 compiler.
* [Hardware design](https://github.com/fossasia/pslab-hardware) : Made with [KiCAD](http://kicad-pcb.org/)
* [Desktop Applications](https://github.com/fossasia/pslab-desktop-apps) : My contributions were towards documenting the various apps and using Jekyll to render markdown files via templates . I cross checked a range of experiments in order to create screenshots, made several schematics, and fixed bugs in a few. I also added applications to calibrate the pslab using ADS1115 16-bit ADC module
* [Python Communication Library](https://github.com/fossasia/pslab-python) : Made bug fixes in capture calls. Helped the android team to understand the various function calls during the porting process. Added support for several new add-on modules such as ADS1115, SX1278 LoRa module, MPU925x 10-DOF IMU sensor among others.
* [remote laboratory](https://github.com/fossasia/pslab-remote) : Made a framework for accessing the PSLab remotely. This involves a backend designed with python flask, and a webapp made with ember-cli. A demo of the webapp hosted on [Surge.sh](pslab-remote.surge.sh), and the backend is hosted on [Heroku](pslab-stage.herokuapp.com)


{% include gallery.html %}

Full list of blog posts I wrote along the way :

+ [The Pocket Science Lab Hardware](http://blog.fossasia.org/the-pocket-science-lab-hardware/)
+ [The Pocket Science Lab: Who Needs it, and Why](http://blog.fossasia.org/the-pocket-science-lab-who-needs-it-and-why-2/)
+ [Temporally accurate data acquisition via digital communication pathways in PSLab](http://blog.fossasia.org/temporally-accurate-data-acquisition-via-digital-communication-pathways-in-pslab/)
+ [Environment Monitoring with PSLab](http://blog.fossasia.org/environment-monitoring-with-pslab/)
+ [Creating Sensor Libraries in PSLab](http://blog.fossasia.org/creating-sensor-libraries-in-pslab/)
+ [Understanding PN Junctions with the Pocket Science Lab](http://blog.fossasia.org/understanding-pn-junctions-with-the-pocket-science-lab/)
+ [Characteristization of Transistors Using PSLab](http://blog.fossasia.org/characteristization-of-transistors-using-pslab/)
+ [Calibrating the PSLab’s Analog Features for Maximum Accuracy](http://blog.fossasia.org/calibrating-the-pslabs-analog-features-for-maximum-accuracy/)
+ [Designing a remote access framework with PSLab](http://blog.fossasia.org/designing-a-virtual-laboratory-with-pslab/)
+ [Creating backend API methods suing Python Flask](http://blog.fossasia.org/designing-a-remote-laboratory-with-pslab-using-python-flask-framework/)
+ [Execute python function calls remotely](http://blog.fossasia.org/designing-a-remote-laboratory-with-pslab-execution-of-function-strings/)
+ [Deploying the API server and Webapp to separate domains automaticaly ](http://blog.fossasia.org/pslab-remote-lab-automatically-deploying-the-emberjs-webapp-and-flask-api-server-to-different-domains/)
+ [Creating better structured apps from user submitted scripts](http://blog.fossasia.org/enhancing-the-functionality-of-user-submitted-scripts-in-the-pslab-remote-framework/)
+ [Adding a graph component to the frontend](http://blog.fossasia.org/including-a-graph-component-in-the-remote-access-framework-for-pslab/)

----

+ The PSLab project is inspired from ExpEYES  <http://expeyes.in>
+ FOSSASIA is supporting development and promotion of ExpEYES project since 2014 mainly through Google Summer of Code

Chat: [Pocket Science Slack Channel](http://fossasia.slack.com/messages/pocketscience/) | [Get an Invite](http://fossasia-slack.herokuapp.com/)


