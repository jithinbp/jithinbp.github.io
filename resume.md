---
title: 
description: >
  <i>"I'm jithin B.P. and I'm a maker and founder at CSpark Research"</i>
hide_description: true
hide_description2: false
menu: true
---


* this list will be replaced by the toc
{:toc .large-only}

{% assign resume = page.resume | default:site.data.resume %}
{% assign basics = resume.basics %}

<header>
  <h1 class="page-title fn p-name" property="name">{{ basics.name }}</h1>

  {% if basics.picture.size > 0 %}
    <img src="{{ basics.picture | absolute_url }}" class="avatar photo u-photo" alt="{{ basics.name }}" property="image" width="120" height="120" loading="lazy" />
  {% endif %}

  {% if basics.label %}
    <p class="h3 faded subline title p-job-title" property="jobTitle">{{ basics.label }}</p>
  {% endif %}

  {% include components/message.html text=page.description hide=page.hide_description2 %}
</header>

{% if basics.summary.size > 0 %}
  <p class="note p-note" property="description">
    {{ basics.summary | markdownify | replace:'<p>','' | replace:'</p>','' }}
  </p>
{% endif %}

  <div class="columns contact">
    {% include pro/resume/basics.html %}
    {% include pro/resume/profiles.html %}
  </div>


## Education

| Year | Education |
| :--- | :--- |
| 2023-2025 | Nava Kerala Chief minister's post doctoral fellowship |
| 2017-2021 | Ph.D. In nuclear physics instrumentation from CUHP |
| 2014 | Masters in Physics from Indian Institute of Science Education and Research, Mohali, CGPA at the end of 10 Semesters – 7.5. |
| 2009 | Higher secondary school examination (XII), CBSE, The Mother’s International school, New Delhi, Aggregate – 87.8% |
| 2007 | Secondary school examination (X), CBSE, The Mother’s International school, New Delhi, Aggregate – 91.4%. |

---

## Awards

| Year | Awards |
| :--- | :--- |
| 2023 | Chief Minister's Nava Kerala Post Doctoral Fellowship |
| 2016 | Google Summer of Code (GSOC) |
| 2007-2009 | Won several awards for Programming and Robotics events at Tech fests in Delhi-NCR. |
| 2008 | Awarded Kishore Vaigyanik Protsahan Yojana (KVPY) Scholarship by Dept. of Sc. and Tech., Govt. of India. |
| 2007 | Awarded Junior Science Talent Search Examination (JSTSE) Scholarship by Dte of Edu., Govt. of New Delhi. |

## [Conferences](/projects/conferences/)

{% include reusables/conferences.md %}

---

## Publications

{% include maketable.html publist=site.data.mypubs  color="green" %}

---

## Computer Skills ([Github](https://www.github.com/jithinbp)) . As of 2013

### Python

* Developed several open source applications for data acquisition and analysis.
    * Point Contact Andreev Reflection Spectroscopy, AC Susceptometry, Virtual Lab, PID control, Cryostat Magnet Control …
* Various Simulations using Numpy, Scipy, OpenCV.
* Parallel Processing as well as Distributive computing.
* Familiar with leveraging supercomputing clusters effectively.
* Other works include remote data acquisition via TCP sockets as well as XMPP based connections.
* Well versed in interfacing scientific equipment with protocols such as GPIB, PCI-e, USB and TCP/UDP.
* Software development for the vLabtool. Includes real time data acquisition, analysis, and visualization.

### C
* Pointers, linked lists, structures, dynamic memory allocation and file handling.
* Applications developed range from an MS-DOS based CAD application and indie games, to fluid mechanics and ODE solvers.

### Embedded C

* Familiar with 16 and 8-bit MCUs from Microchip. Used them in conjunction with analog circuitry to develop low cost test and measurement equipment.
* Worked with developing firmware for a Multi Channel Analyzer based on an ATMEGA32 chipset.
* Getting acquainted with the ESP8266 low cost Wi-Fi chipset.

### Interfacing Scientific Equipment

* Working experience with a host of high end tools from KEITHLEY, Lakeshore, AMI, RHK, and SRS.
* Developed dedicated standalone applications for transport and spectroscopic measurements as part of my Master’s Thesis work.
* Presently working on an educational toolsuite targeted at physics and electronics teaching labs.
* Driven towards using open-source tools wherever possible, instead of restrictive and proprietary environments such as LabVIEW.
* Experience includes TCP/UDP, GPIB, USBTMC, RS-232, EUSART, SPI, I2C and IR.

### C++

* Classes, pointers, stacks, queues and dynamic memory allocation.

### Java

* [Go to My Google Play Store Showcase](https://play.google.com/store/apps/developer?id=Jithin+BP&amp;hl=en)
* [Running ExpEYES](https://play.google.com/store/apps/details?id=com.expeyesexperiments) on Android devices with USB OTG.
* An Android based [web server for ExpEYES](https://play.google.com/store/apps/details?id=com.expeyesserver).
* [A Data Logger](https://play.google.com/store/apps/details?id=com.scpi) for Instruments that use SCPI commands and have Ethernet Connectivity.

### Linux

* Ubuntu is my go-to OS for just about all my software and coding needs.
* Familiar with a variety of distros including Fedora, SUSE, Mint, and Slackware.
* Kernel compilation for A13 based tablets, Raspberry Pi, and custom Real Time Schedulers.
* Cloud setup with NFS sharing and NIS authentication.

### Web Development

* Apache, PHP, PHP-gd, DRUPAL CMS, Mod-python, Python-PSP, CherryPy, JavaScript, Jquery and AJAX.
* Applications developed include a Drag and Drop programming interface, Webapps for scientific equipment, and embedded HTML in Qt Apps.
* Designed this website, so I have a fair amount of WordPress familiarity.

### Database Management

* Sqlite3
* MySQL

### Office Tools

* LibreOffice / Open Office
* LATEX

### Miscellaneous

* PERL
* REGEX
* CGI, and SHELL scripting

---

## Summer Projects (Pre-2014)

### 2013 - July: Remote Access for the Particle Accelerator framework, IUAC

* Implemented a CherryPy based web server which hosts a dynamic, Jquery and AJAX based website to allow control and monitoring of various parts of the particle accelerators via the control system.


### 2013 - May, June: Techniques in Condensed Matter Physics. Dr. Goutam Sheet, IISER Mohali

* Pulsed laser deposition of YBCO and SrRuo3 thin films. Sputter deposition of copper on insect wings.
* Developed data acquisition software for superconductivity transition measurements using Lock-in amplifiers.
* Compiled RTOS linux kernel for running PID loops for stabilizing tunnelling currents in STMs. Set up COMEDI drivers.


### 2012 - summer: Instrumentation and radiation detection. IISER Mohali, IUAC

* Characterized crystal oscillators using a network analyser at The Ultra low temperature lab, IISER Mohali.
* Developed electronics for driving a Geiger Muller tube and a Photomultiplier tube.
* Extracted Thorium from Thorium nitrate for educational experiments.

### 2011 summer: Developing an MCA for Alpha particle detectors. IUAC, New Delhi

* Developed firmware for an Atmega32 based MCA. Coded features include segregation based on peak energy, reading and writing from CMOS memory, and USB communication. Developed a Python-Tk based GUI. Calibration was carried out using Co-60.

### 2011 summer: Scanning Tunneling Microscopy. IUAC, New Delhi. Quazar Tech, New Delhi

* Learnt about the design and construction of the instrument from its developers, and obtained atomic resolution scans of HOPG. Visited the manufacturing facility.

### Summer 2010: Virtual Lab Project. IIT Kanpur, Dr. Anjan Gupta

* Worked on developing a fully open source framework for controlling instruments remotely. Successfully hosted a resistivity measurement setup on the Intranet. A real time plot server for web browsers was developed. An oscilloscope interface was also made as part of this project.

### 2009: Senior Secondary School Exam - Project Work

* Authored C++ based football video game with 8-bit VGA graphics. Standard Human Vs. Computer mode where the PC is capable of making decisions to coordinate its players.

### 2009 Summer: Electrodeposition and characterization of FeAu thin films. IIT Delhi, Dr. Ratnamala Chatterjee

* Thin film deposition of Iron-Gold alloy films by using electro-deposition and subsequent Characterisation using X-ray diffraction and atomic force microscopy.


### 2007: 3D modelling software based on Ms-dos graphics.

* Authored an interactive C program to create 3D drawings using basic shapes. Employs dynamic memory allocation, structures, and basic trigonometry to rotate the models.

### 2007: Sci-ELF robot - Atmega32 based line follower

* Atmega32 based line follower developed for the science fair at The Mother’s International School.


---

### Coursework Related Projects

* Simulation of mixing of ideal gases, Prof Jasjeet Bagla
    * Simulation of ideal gases mixing in an adiabatic box, and extracting thermodynamic data such as pressure and velocity distribution.
* Developing interactive software for simulating and viewing 3-Dimensional phase portraits, Dr. Sudeshna Sinha
    * Allows configuring equations for X,Y and Z directions. Lorentz attractor equations fed as default. Also simulated fractals.
* Low temperature PID controller, Dr. Ananth Venkatesan
    * Implemented a software PID loop in Python which was capable of stabilizing the temperature within a 25 milliKelvin error. Tested from 77K to 100K. Measured the temperature dependence of a carbon film resistor.
* Simulation of Blonder, Tinkham, Klapwikj theory plots, Dr. Goutam Sheet.
    * Simulated results of the BTK theory of transport phenomena across a metal-superconductor interface by using Python-Numpy and PyGrace.
* Real time tracking of a sensitive torsion pendulum, Dr. K.P. Singh
    * Developed an OpenCV based Python program to monitor a torsion pendulum in real time and hosted a dynamic web page to monitor oscillation plots and video feed.
* Masters Thesis: Scanning Tunneling Microscopy and Transport Spectroscopy at Low temperature, Dr. Goutam Sheet, IISER Mohali
    * Worked on my Masters thesis during the Academic Year 2013-2014. Developed several instruments, as well as learned several techniques dealing with low-temperature, high vacuum environment physics. Developed software and probes for Point Contact Andreev Reflection Spectroscopy, as well as a room temperature Scanning Tunneling Microscope.

---

## Hobby Projects, and Open Source Contributions

* A Versatile Labtool
    * A cost effective, multi-pronged data acquisition tool aimed at schools and colleges. It was in the running for the Hackaday Prize 2015, and won a few [prizes](http://hackaday.com/2015/07/07/50-winners-using-microchip-parts/) [too](http://hackaday.com/2015/07/06/50-winners-using-texas-instruments-parts/).
* Python Powered Scientific Instrumentation Tool
    * This work was presented at Scipy.in, an Intl. Conf. on Scientific Computing in 2014.
    * The tool-suite includes an oscilloscope, a logic analyzer, several waveform generators, and the ability to interface with a wide variety of digital and analog sensors.
    * It was also favorably reviewed on [Hackaday.com](http://hackaday.com/2015/06/05/hackaday-prize-entry-python-powered-scientific-instrumentation/), and won several awards as part of the events leading up to the quarterfinals of the Hackaday Prize 2015.
* Android applications for the ExpEYES toolkit.
    * Developed and published on the Play Store, Android applications for connected expEYES devices. Implemented several experiments and features.
* Android Application for data acquisition and visualisation from TCP enabled Scientific Instruments.
* Web browser based drag and drop programming interface.
    * Based on a Jquery+AJAX frontend, and a CherryPy,Linux-GPIB,OpenCV,Python-usbtmc Backend.
* OpenCV based Motion sensing security camera.
    * Logs video clips. Alerts over GChat IRC using xmpppy.
* Developing a web interface for ExpEYES low cost instrumentation tool.
* Cluster Computing in Python
    * Simulated the Ising model using the supercomputing cluster via multiprocessing in Python.
* Advanced Quiz buzzer system with a USB interface.
    * An ATMEGA32 based device developed for the IISER Mohali quiz club.
* Money managing system for fundraising events.
    * Python-xmpp based program maintains a database of all potential funders.

---

## Other Skills and Interests

| | Other Skills and Interests |
| :--- | :--- |
| Languages | English, Hindi, Malayalam, Basic French |
| Music | Sangeet Bhushan for vocal classical (Pracheen Kala Kendra). Guitarist. Owner and tinkerer of many other instruments. |
| Sports | Football, Volleyball, Badminton |

