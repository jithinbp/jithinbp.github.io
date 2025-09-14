---
layout: project
title: 'Scanning Tunneling Microscope'
date: 20 Oct 2013
image:  
  path: /assets/img/stm/stm.jpeg
screenshot: /assets/img/stm/stm.jpeg
caption: Room temperature scanning tunneling microscope with Attocube walkers and R9 PID.
description: >
    Part of my thesis work involved developing a room temperature prototype of a scanning tunneling microscope(STM).
    Please refer to the full text of my thesis for a more elaborate write-up
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#1c1c1c 0%,#5d5e59 30%,#9d9f94 50%,#a4988e 70%,#984406 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}

## Room temperature STM : Preliminary readings

The STM was used to study the structure of Highly ordered pyrolytic graphite(HOPG) at room temperature, and monolayer steps were imaged. The thickness of each layer was estimated to be around 100 picometer. IV spectroscopy was also conducted on the surface of HOPG .


### Measurements

* Coarse Approach : Attocube nanopositioner with ANC300 controller.
* Scanning :    Axially segmented piezo tube from Physik Instrumente
* Control Electronics : R9 from RHK.  Software written in IHDL
* Vibration Isolation : Heavy platform suspended inside an empty instrument rack via bungee cords
* Tip Holder : Hypodermic needle.
* Matching piece (for Attocube Walker and Piezo tube) :  Eventually settled on Delrin since Macor isn’t easy to procure, and the local machinists aren’t familiar with it.
* Guide rails : machined from SS rods.
* Electrical shielding : SS sheet metal construction.

![Full-width image](/assets/img/stm/stm_labels.png){:.lead width="400" height="100" loading="lazy"}
Image :  The assembly and its various parts.
{:.figcaption}


![Full-width image](/assets/img/stm/readings.png){:.lead width="400" height="100" loading="lazy"}
Various measurements on standard calibration samples
{:.figcaption}




![Full-width image](/assets/img/stm/scan1.jpeg){:.lead width="400" height="100" loading="lazy"}
First scan from my STM. on a standard sample that came with the AFM from Asylum Research
{:.figcaption}


![Full-width image](/assets/img/stm/gold.jpeg){:.lead width="400" height="100" loading="lazy"}
Layers on a gold film imaged with this STM. The film was sputtered and annealed.
{:.figcaption}

## Low temperature probe design

![Full-width image](/assets/img/stm/lowtemp.png){:.lead width="800" height="100" loading="lazy"}
With a liquid helium cryostat expected to arrive soon , I proceeded to design a probe compatible with its dimensions, and capable of housing the scanning probe
{:.figcaption}


The drawing was made using SolidWorks, and the scanning probe included an additional linear positioner that would allow moving to a cleaner region without disturbing the cryostat, vacuum etc.
The Cryostat was purchased from American magnetics, and features a 3-axis vector magnet.  The vertical field can be set to a maximum of 6 Tesla, while vector fields are limited to 1 Tesla.

![Full-width image](/assets/img/stm/cryo.jpeg){:.lead width="400" height="100" loading="lazy"}

In order to ensure uninterrupted Liquid Helium supply , a helium plant with two 160 liter portable liquefiers was set up in an adjacent building.  Helium transfer needs to carried out every 3-4 days, and is usually managed by the undergrads.  I need to write a page dedicated to this cryostat, its vibration isolation pit, and RF shielding soon.


### Later developments

After I left, a low temperature MFM probe was also installed. got some photos during a later visit.

![](/assets/img/blog/spm1.jpeg)
![](/assets/img/blog/spm2.jpeg)
![](/assets/img/blog/spm3.jpeg)