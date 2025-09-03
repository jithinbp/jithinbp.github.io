---
layout: project
title: 'Point Contact Spectroscopy'
date: 20 Oct 2013
image:  
  path: /assets/img/pcar/pcar_thumb-578x330.jpg
screenshot: /assets/img/pcar/pcar_thumb-578x330.jpg
caption: Electronic transport across nano-constrictions
description: >
    I did some work on point contact spectroscopy to study band gaps in superconductors. The image shows a gold film with a Niobium needle forming a point contact.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#3b2300 0%,#c0ac6c 30%,#f2d88e 50%,#f4de8c 70%,#cdccc8 100%)'
  background-old: 'linear-gradient(to bottom,#193747 0%,#233e4c 30%,#3c929e 50%,#d5d5d4 70%,#cdccc8 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}




## Electronic transport across nano constrictions

Contacts between conductors can be classified based on their radius , and the smallest radius possible for a conducting pathway is limited by the de-Broglie wavelength of the electron (Topinka 2000). Electrons flowing through conductors wider than the mean free path routinely undergo scattering by phonons and other elementary excitations, but the current-voltage characteristics of this form of transport, commonly known as bulk transport, is the result of scattering of these electrons whose momenta are spread out over the Fermi surface. Instead, when a nano-constriction with width less than the mean free path is used, statistically speaking the electrons can be assumed to undergo zero scattering (Nikolic and Allen 1998). In such a case, the kinetic energies of electrons being scattered can be defined as a function of the potential difference(V) across the constriction. This allows energy resolved spectroscopy of the elementary excitations by measuring the current-voltage characteristics of such a junction (Jansen, Gelder, and Wyder 1980).

The “Needle-Anvil” method employed by our instrument setup is the simplest for forming nano-constrictions (Janson et al. 2012). A needle like conductor is brought into contact with a flat conductor using a precise mechanical assembly to make cracks in existing oxide layers resulting in the formation of conduction pathway of a very small radius. The resulting point-contact acts as a local probe, wherein the electrical transport is affected by the scattering processes occurring within the local neighbourhood of the contact (Erts et al. 2000).

![Full-width image](/assets/img/pcar/probe2.png){:.lead width="800" height="100" loading="lazy"}

Conductance varies from the Sharvin regime for purely ballistic contacts to the Maxwell regime for bulk transport (Nikolic and Allen 1998). Purely diffusive contacts are described by the Ohm’s Law, where resistance is given as a function of the resistivity, the area of cross section, and the length of the conductor.

Conductance across contacts can be compared with the problem of gas flowing between two chambers with unequal pressures via a small orifice. When the dimensions of the orifice(a) are less than the path length(l) of the gas molecules, diffusive flow assumptions are no longer valid, and ballistic transport occurs. This problem was first studied by Knudsen(1984), and the Knudsen ratio (l/a ) is used to describe the various transport regimes.

## Design and construction of the probe

![Full-width image](/assets/img/pcar/probe.png){:.lead width="800" height="100" loading="lazy"}


![Full-width image](/assets/img/pcar/pcar_cernox.jpg){:.lead width="800" height="100" loading="lazy"}

## Testing and Instruments


![Full-width image](/assets/img/pcar/setup.jpg){:.lead width="800" height="100" loading="lazy"}

Full setup for my experiment.
{:.figcaption}

![Full-width image](/assets/img/pcar/PCAR_flow.png){:.lead width="800" height="100" loading="lazy"}

![Full-width image](/assets/img/pcar/software.png){:.lead width="800" height="100" loading="lazy"}

Software I wrote for this work. Uses linux-gpib to speak to the temperature controller, the voltmeters, sources and stepper motor.
{:.figcaption}

![Full-width image](/assets/img/pcar/B_field_3T.png){:.lead width="800" height="100" loading="lazy"}

Influence of 3 Tesla Magnetic field on the differential conductance.
{:.figcaption}
