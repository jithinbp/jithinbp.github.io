---
layout: project
title: 'Virtual Lab Project'
date: 20 Oct 2012
image: /assets/img/thumbs/virtual-lab-iit-kanpur-cover.png
caption: Virtual Lab I developed with Python PSP at IIT Kanpur
description: >
    The general aim of this project was to hook up all lab instruments necessary for a particular experiment onto a server so that select users present at a remote locations can access and set parameters on these instruments and view the results on an interactive web page in real  time(web traffic delays overlooked). The entire software set-up and drivers used here are open source based as opposed to the proprietary LabView platform from National Instruments, so as to allow lay users easy access to designing experiments.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#3b2300 0%,#c0ac6c 30%,#f2d88e 50%,#f4de8c 70%,#cdccc8 100%)'
  background-old: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}

## Overview

The virtual lab project aims to allow scientific folk with limited resources or otherwise, access to all necessary equipment hooked up to a common server, the controls to which are hosted by it on a web-page which has the necessary framework enabling them to set parameters, obtain readings etc.
The operating system running on the server is Debian GNU/Linux. Coding platforms include Python, Python-psp, PHP, PHP-Gd ,Java Script and HTML. TCP/IP sockets were a life saver when it came to client-server communication

Clients have access using any OS but must have JavaScript enabled on their browsers in order to be able to use the interactive environment and view dynamically refreshed plots and data sent by the server. Instruments connected to the server use the GPIB Interface to communicate with it.

![Full-width image](/assets/img/mastersacad/virtual-lab-homepage.png){:.lead width="800" height="100" loading="lazy"}


The GPIB dongle interfacing the instruments used in this project is manufactured by National Instruments.
The main page of the virtual lab project provides the user with a list of web-pages which host different experiments, and on being selected, these are displayed in an interactive frame on the same page itself. All users may view the readings but only those with authorization may set controls on the devices after identifying themselves by means of a password.
Since web browsers are not allowed to keep TCP/IP sockets alive, the user has to send in authorization details each time parameters of an ongoing experiment need to be modified. The method also has the advantage of not restricting the user to a particular network address.changed may be made from different locations . The program running on the server which deals with accessing the instruments keeps track of which user is controlling a particular experiment. Although, all users can view
readings in real-time (ignoring web-traffic delays).


## Oscilloscope

![Full-width image](/assets/img/mastersacad/virtual-lab-iit-kanpur-oscilloscope.png){:.lead width="800" height="100" loading="lazy"}
A simple Oscilloscope using ADC readings from ATMEGA16 microcontroller based device “PHM” communicating via USB.
{:.figcaption}

The user is allowed access to a webpage that displays a dynamically refreshed graph-plot of ADC data and an accompanying form with fields[name , password, samples, delay and cycles] which he may fill and submit to a queue of requests from other users stored in a database on the server. A real time plot with parameters set by the first user in the queue is visible. The entry is deleted on completion of the experiment and the next entry in the queue is executed.

### Workflow.

The user adds his choice of parameters to a database. This database is accessed by a program running on the server and this program then writes a bunch of data onto a datafile continuously updating it with new readings. This file contains the latest readings from the oscilloscope.

A PHP script generates a plot of this data and creates a png image of it using PHP-GD each time it is run and it also zooms the plot according to a zoom variable passed to it which may vary from fixed values to auto zoom wherein it zooms the Y- axis to the image size.

The user’s web page displays this plot which includes details like the user-name,zoom and other parameters and it is continuously refreshed using javascript so as to give an impression of a real oscilloscope.


## IV Characteristics

Resistance versus Temperature Characteristics study using LakeShore 336 Temperature Controller and KEITHLEY 2001 Multimeter

Again, the user is allowed can access a webpage that displays experiment reults as a plot and an accompanying form with fields[name , password, samples, starting temperature and ending temperature] which they may fill and submit by connecting to a socket created by a program running on the server which actually handles the instruments and data.

The user is required to provide authorization details and may take control of the experriment if no other user is controlling it. A real time plot which is refreshed continuously is visible on the page.
They may also modify certain parameters while the experiment is in progress by reconnecting to the server, providing identification and then requesting necessary changes.


![Full-width image](/assets/img/mastersacad/virtual-lab-iit-kanpur-temperature-dependence.png){:.lead width="800" height="100" loading="lazy"}
A simple Oscilloscope using ADC readings from ATMEGA16 microcontroller based device “PHM” communicating via USB.
{:.figcaption}

### How it works.

A program running on the server ( restemp_server.py) creates and binds a socket to the host IP address and it then proceeds to wait for users who may want to connect and take control of the experiment which involves measuring resistance of a sample over a certain temperature range. Once a user connects, it reads a stream of data from it and initiates the experiment. This stream of data contains authorization details, and parameters for the experiment. It also has provision for writing a custom command to the device. The data is continuously fed into a datafile restemp.dat. Each time a client connects, it must identify itself ,and the changes requested by it are carried out only if the server decides to comply. The file restemp.dat contains the latest readings from the oscilloscope. A PHP script(restemp.php) generates a plot of this data and creates a png image of it each time it is run. The users’ web page displays this plot which includes details like the user-name and other parameters and it is continuously refreshed using javascript so as to give an impression of a real time plot.

Source codes to the programs written for this particular purpose are attached. These include

* restemp.psp -the client page
* restemp_server.py- the mediator program running on the server
* restemp_plot.php – graph generator


#Author : Jithin B.P.
Indian Institute of Science Education and Research (IISER) Mohali,
Chandigarh , India
contact the author:
jithinbp %$# gmail com

 

ToDo: Insert complete instructions for setting up apache for python-psp, and also linux-gpib. Just google the heading text to locate the full pdf report I had submitted at the end of this summer project.