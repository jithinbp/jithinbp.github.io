---
layout: project
title: 'Sastrayan 2026 Website Dev'
date: 22 Jan 2026
image: 
  path: /assets/img/sastrayan/sastrayanwebcover.jpeg
caption: Website for coordinating sastrayan
description: >
  Magnetic Levitation experiment
accent_color: '#4fb1ba'
accent_image:
  background: 'url(/assets/img/sastrayan/cover2.jpeg)'

---

## Sastrayan 2026 Website Dev


The open house event sastrayan involved 30+ departments and offices of the university. consolidating everything on a common
platform was required in order to present an event map to the public and also estimating funds utilisation in real time.

I implemented the following on a python flask based backend and a vanilla JS html frontend which uses openstreetmaps

+ Event map for the public. All events are shown as markers on an OSM map with leaflet.js . clicking them pops up the event brochure image if the respective department has uploaded it.

![](/assets/img/sastrayan/sidebanner.jpeg)

+ Login feature where the page auto redirects to a hosting page when the email of a Head of department is used. e.g. , hodphy@uoc.ac.in will automatically go to the registration page where they can fill out details of events that physics department is planning. For other emails it goes to a regstration page for schools where school in charges can submit the number of students they are bringing, and the consolidated contact CSV was shared with volunteers.

![](/assets/img/sastrayan/userdashboard.png)


+ Admin can view net fund requirement, resource requirement, lat-long for each event etc. there are also view-only admins like the PLD who can monitor fund requirements.

![](/assets/img/sastrayan/admindashboard.png)

