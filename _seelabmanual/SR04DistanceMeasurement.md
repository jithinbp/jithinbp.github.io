---
layout: manual
title: "Distance Measurement using SR04 Ultrasonic Module"
date: 31 March 2026
image:
  path: /assets/img/seelab/mechanics/images/sr04-setup-seelab3.jpg
caption: SR04 module measuring distance to moving reflector
section: Mechanics
---

## Experiment: Measuring Distance using SR04

### 1. Aim

To measure distance versus time with SR04 and use the data to estimate oscillation frequency of periodic motion.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* HC-SR04 ultrasonic sensor module
* Hard reflecting surface / mass-spring setup / pendulum target
* Connecting wires
* Python scripts (`sr04.py`, `sr04-analyse.py`)

---

### 3. Theory & Principle

SR04 emits ultrasound and detects echo return time. Distance is obtained from time-of-flight of sound pulse. ExpEYES function:

`tm, dist = p.sr04_distance_time()`

For periodic motion, distance-time data can be fit to sine function to obtain frequency and period.

---

### 4. Circuit Diagram / Setup

1. Wire SR04 as shown in the ExpEYES setup.
2. Place a flat reflecting target in front of sensor.
3. Move target periodically (hand oscillation / spring-mass / pendulum).

---

### 5. Procedure

1. Run acquisition for ~5 seconds and save data to `sr04.csv`.
2. Plot distance vs time.
3. Select a clean oscillation segment.
4. Fit to sinusoid and extract frequency.
5. Compare measured period with theoretical model (if applicable).


<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/sr04-screen-phone.jpg" alt="Transistor Amplifier - Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Measurements Screenshot</p>
    </div>
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/sr04-pendulum.jpg" alt="Transistor Amplifier - Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Setup Photo</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | Mean Distance (cm) | Frequency (Hz) | Period (s) | Remarks |
| :---: | :---: | :---: | :---: | :--- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

### 7. Results and Discussion

* Distance tracking was successful over the 5 s acquisition window.
* Sinusoidal fit provided oscillation frequency of ________ Hz.
* Method works well for periodic systems with strong reflective surfaces.

---

### 8. Precautions

1. Keep reflector flat and roughly perpendicular to sensor.
2. Avoid nearby moving objects causing false echoes.
3. Ensure target remains within SR04 sensing range.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Unstable distance values | Weak/angled reflector | Use larger flat target |
| Missing points | Out-of-range target | Keep target within rated range |
| Poor fit quality | Non-periodic motion | Use cleaner oscillatory motion |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why use curve fitting instead of a single peak count?</b></summary><p><b>Ans:</b> Fitting uses all samples, reducing random error in frequency estimation.</p></details>
<details><summary><b>Q2. Can SR04 measure static distance accurately?</b></summary><p><b>Ans:</b> Yes, if alignment and reflection quality are good, 3mm step size can be expected. For poor quality surfaces, 5mm +/- variations can be seen.</p></details>
</div>

