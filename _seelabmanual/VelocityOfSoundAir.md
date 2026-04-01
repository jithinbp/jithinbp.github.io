---
layout: manual
title: "Velocity of Sound in Air"
date: 31 March 2026
image:
  path: /assets/img/seelab/sound/images/sound-vel-setup1.jpg
caption: Phase comparison between WG reference and microphone signal
section: Acoustics
---

## Experiment: Velocity of Sound in Air

### 1. Aim

To determine velocity of sound in air using phase difference between reference waveform and microphone signal.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* Piezo buzzer (sound source)
* Microphone/pressure sensor
* Scale/ruler
* Stands and connecting wires

---

### 3. Theory & Principle

For a sinusoidal wave:

$$v = f\lambda$$

If two positions differ by 180 degrees phase, separation equals $\lambda/2$.

Hence:

$$v = 2f\Delta x$$

where $\Delta x$ is distance shift between in-phase and out-of-phase conditions.

---

### 4. Circuit Diagram / Setup

1. Drive piezo with WG at fixed frequency (around 3400 Hz).
2. Measure WG as reference and MIC as received signal.
3. Move microphone along the source axis and monitor phase relation.

---

### 5. Procedure

1. Set WG frequency near buzzer resonance.
2. Find microphone position where WG and MIC are in phase.
3. Find position where they are 180 degrees out of phase.
4. Measure displacement $\Delta x$ between these positions.
5. Compute velocity: $v = 2f\Delta x$.
6. Repeat multiple times and average.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/sound/images/sound-vel-screen1-phone.jpg" alt="Velocity of Sound - Mobile Screen 1" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 1</p>
    </div>
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/sound/images/sound-vel-screen2-phone.jpg" alt="Velocity of Sound - Mobile Screen 2" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 2</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | Frequency $f$ (Hz) | In-phase position (cm) | 180 degrees position (cm) | $\Delta x$ (m) | $v=2f\Delta x$ (m/s) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

---

### 7. Results and Discussion

* Measured velocity of sound: ________ m/s.
* Value is affected by reflections and alignment errors.
* Measurement quality improves in open space with fewer reflecting surfaces.

---

### 8. Precautions

1. Keep source and microphone collinear.
2. Minimize reflections from nearby walls/objects.
3. Use stable frequency and avoid touching setup during measurement.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Phase relation unclear | Weak signal or noisy environment | Increase signal level and reduce ambient noise |
| Unrealistic velocity | Distance reading error | Re-measure positions carefully |
| Unstable waveform | Poor microphone placement | Fix sensor position and orientation |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why does 180 degrees phase shift correspond to half wavelength?</b></summary><p><b>Ans:</b> A full wavelength corresponds to 360 degrees; half of it gives 180 degrees.</p></details>
<details><summary><b>Q2. Why are results often slightly high/low?</b></summary><p><b>Ans:</b> Reflections and phase-reading uncertainty shift effective path difference.</p></details>
</div>

