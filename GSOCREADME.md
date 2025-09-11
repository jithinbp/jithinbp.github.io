# GSOC 2017

This page is for my GSoC-2017 work

For GSoC-17, I contributed much of my work from 2014 onwards on the ExpEYES project to the PSLab project. Given that the contributions
were hijacked, and neither I not any of the original developers no longer receive any credit, this only serves as an archive. I now contribute
directly to the ExpEYES project by :

+ maintaining the [Desktop apps](https://github.com/expeyes/expeyes-programs/)
+ writing the [android app](https://play.google.com/store/apps/details?id=com.cspark.research.eyes17) which is currently more mature than the desktop UI
+ Maintaining a [programmer's manual](https://readthedocs.org/projects/eyes17lib/)
+ Updating the firmware

## GSOC contributions

### Firmware : https://github.com/fossasia/pslab-firmware 

Code for PIC24E processor written with MPLab IDE and compiled with XC16 compiler. This was from my SEELablet project documented on Hackaday as [Python Powered Scientific Instrumentation tool](https://hackaday.io/project/5971-python-powered-scientific-instrumentation-tool/details)
and on github as [Labtoolsuite](https://github.com/jithinbp/LabToolSuite)

+ Hardware https://github.com/fossasia pslab-hardware : Made with [KiCAD](http://kicad-pcb.org/) by Dr Ajith Kumar for [Vlabtool](https://hackaday.io/project/6490-a-versatile-labtool), a more mature version of the previous one.
+ Desktop application: https://github.com/fossasia pslab-desktop-apps : A clone of [SEELablet](https://lists.debian.org/debian-devel/2016/01/msg00032.html) which was already available on the official Debian repository.
+ Python Communication Library : Was also a part of the previous one.
+ remote laboratory : https://github.com/fossasia pslab-remote : Made a framework for accessing the device remotely. This involves a backend designed with python flask, and a webapp made with ember-cli. A demo of the webapp hosted on  surge, and the backend is hosted on Heroku.

A list of blog posts I wrote elaborating my journey (The most useless part of this GSOC where all they wanted was publicity for their organisation) :

+ Who Needs it, and Why the-pocket-science-lab-who-needs-it-and-why-2/
+ Diode IV understanding-pn-junctions-with-the-pocket-science-lab/
+ Calibration calibrating-the-analog-features-for-maximum-accuracy/
+ Transistor CE characteristization-of-transistors-using-pslab/
+ Remote lab framework designing-a-virtual-laboratory/
+ Creating backend API methods with  Python Flask designing-a-remote-laboratory-using-python-flask-framework/
+ Execute python function calls remotely designing-a-remote-laboratory-with-execution-of-function-strings/
+ Deploying the API server and Webapp to separate domains automaticaly 

----

+ The PSLab project is derived from ExpEYES  <http://expeyes.in>
+ FOSSASIA is riding off the back of ExpEYES project through Google Summer of Code
