---
layout: projects
title: Masters at IISER Mohali
show_collection: iiser
image:  
  path: /assets/img/pcar/thermal.png
screenshot: /assets/img/pcar/thermal.png
---

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiser | sort:"date"%}
{% for project in ordered_projects limit:3 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

### The Following is the introductory section from my Masters thesis work during the academic session 2013-14

>  Scanning tunneling microscopes(STM) are instruments capable of extremely high spatial resolution down to sub-angstrom length scales. Their capabilities range from imaging lattice structures, to observing standing wave pattern of surface state electrons in metals, and spatial manipulation of individual atoms. Plainly speaking, they let us ’see’ atoms, move them around, and more. Additional capabilities have also been developed for STMs, such as spin polarized tunneling microscopy, and the ability to spatially manipulate of single atoms. A prerequisite for high resolution imaging, is an atomically sharp probing tip, preferably with a p z or d 2 z orbital at the apex. From the position-momentum uncertainty(∆x.∆k x ≥ 2π), it can be inferred that such a small value for ∆x will result in a large error in momentum information(∆k) . In order to increase the resolution in momentum, dull tips are preferred for acquiring spectroscopic data.

> Point Contact Spectroscopy is a technique to measure the electronic structures in solids by fabricating nano-metre sized ’ballistic’ contacts between conductors, and measuring the current-voltage characteristics. In keeping with the position-momentum uncertainty, the large size of the contacts makes it a very powerful spectroscopic tool that is used to measure elementary excitation spectra in conducting solids. The IV spectra is used to reveal information regarding the excitation energies of phonons, magnons, quasi-particles in superconductors etc. This technique when applied to nano-constrictions formed between metals and superconductors, can be used to extract the superconducting energy gap by fitting with theoretical formalisms, and this is known as Point Contact Andreev Reflection(PCAR) Spectroscopy.

> During the course of this thesis, I have developed two major instruments for investigating the physical properties of solids down nano-metre length scales at low-temperatures and high magnetic fields.

> A scanning tunneling microscope was developed and calibrated. It was also used to image atomic steps in Highly Oriented Pyrolytic Graphite(HOPG), as well as obtain IV spectra.

> A low temperature probe for carrying out point contact spectroscopy was also developed in-house, and used with a liquid helium cryostat. Experiments were carried out to study the temperature and magnetic field dependence of F eT e 0.6 Se 0.4 -Silver point contacts. Andreev reflection spectroscopy was also carried out in Niobium-Gold point contacts.



Full Text of my dissertation submitted to IISER Mohali towards completion of BS-MS dual degree. [Download](/assets/pdf/jithin_ms_thesis.pdf)


## Academic Projects

<div class="columns mt3 {% unless no_third_column %}columns-break{% endunless %}">
{% assign ordered_projects = site.iiseracad | sort:"date" | reverse %}
{% for project in ordered_projects limit:3 %}
    {% assign featured = page.featured | default:project.featured | default:page.big_project | default:project.big_project %}
    <div class="column column-1">
    {% include_cached pro/project-card.html project=project featured=featured %}
    </div>
{% endfor %}
</div>

<p class="read-more mt1"><a class="heading flip-title" href="/iiseracad/">More about Academic projects I worked on at IISER</a></p>

## MS Thesis work
