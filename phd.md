---
layout: project
title: Ph.D. Work
date: 1 Dec 2020
thumb: /assets/img/phd/coincidence.webp
tl: 49%
tw: 38%
image:  
  path: /assets/img/phd/coincidence.jpg
caption: Summary of my Ph.D. dissertation
description: >
    A gamma-gamma coincidence setup developed as part of my Ph.D. work. The spectrum shows coincidence of positron annihilation events from a <sup>22</sup>Na source placed between two detectors.
accent_image:
  background: 'url(/assets/img/bg2.jpg)'

---


## Ph.D Dissertation

>   The goal of this thesis is to design, develop, and deploy equipment along with novel
    experiments with high instructional value essential for research and education in the field
    of nuclear radiation physics. This field is largely constrained by high equipment prices
    driven by a shortage of indigenous intellectual property as well as local manufacturing,
    and as a consequence gets minimal hands-on instruction in the vast majority of science
    institutions across India.
    We have compiled a list of essential equipment critical for tackling this challenge, and
    have developed the necessary detector technology, electronics designs, and complementary
    firmware and software code to keep costs at a minimum. Additionally, our designs have
    been validated with experiments with pedagogical value performed using the final devices.
    The key instruments developed are a USB powered multi-channel analyzers(MCA)
    for measuring energy spectrum, Alpha Particle and Gamma Ray spectrometers with signal
    processing electronics, and a Gamma-Gamma coincidence measurement setup. Addition-
    ally, a detector array, and a portable cellphone powered gamma spectrometer design has
    also been explored.
    The significance of this study lies in the completeness of the developed instruments
    including technical and scientific documentation, and their demonstrated ability to be
    deployed to universities for teaching and research.


* You can download the [slides for my final presentation](/assets/pdf/jithin_phd_slides.pdf)
* Or my [Ph.D. thesis](/assets/pdf/jithin_phd_thesis.pdf)

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.phd | sort:"date" | reverse %}
{% for project in ordered_projects %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>
