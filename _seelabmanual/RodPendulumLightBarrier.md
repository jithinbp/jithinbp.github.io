---
layout: manual
title: "Pendulum Period using Light Barrier"
date: 31 March 2026
image:
  path: /assets/img/seelab/mechanics/images/rodpend-setup-seelab3.jpg
caption: Rod pendulum crossing LED-phototransistor light barrier
section: Mechanics
---

## Experiment: Pendulum Period using Light Barrier

### 1. Aim

To measure pendulum time period with high precision using a light barrier and estimate acceleration due to gravity.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* White LED (source)
* Phototransistor (detector)
* Rod pendulum and support stand
* Connecting wires and ruler
* Python/SEELab interface

---

### 3. Theory & Principle

When the pendulum interrupts light between LED and phototransistor, SEN changes logic level. Timing the successive transitions gives period:

$$T = \frac{t_{2\ cycles}}{2}$$

For a simple pendulum:

$$T = 2\pi\sqrt{\frac{L}{g}}, \qquad g=\frac{4\pi^2L}{T^2}$$

ExpEYES reports period spread around $0.1\text{ ms}$, enabling amplitude-dependence studies.

---

### 4. Circuit Diagram / Setup

1. Connect LED between **SQ1** and GND (SQ1 has internal 100 Ohm series resistor).
2. Connect phototransistor collector to **SEN**, emitter to GND.
3. Place pendulum so it cuts the light path during oscillation.
4. Test wiring by pulsing SQ1 and observing SEN response.

---

### 5. Procedure

1. Align LED and phototransistor for clear light interception.
2. Set pendulum oscillation at small amplitude.
3. Measure period repeatedly via GUI/Python (`multi_r2rtime('SEN', 2)`).
4. Record at least 10 values and compute mean and spread.
5. Use measured $T$ and pendulum length $L$ to estimate $g$.
6. Repeat for larger amplitudes and compare period change.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/rodpend-screen1-phone.jpg" alt="Rod Pendulum - Mobile Screen 1" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 1</p>
    </div>
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/rodpend-screen2-phone.jpg" alt="Rod Pendulum - Mobile Screen 2" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 2</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | Length $L$ (m) | $T$ (s) | $g=4\pi^2L/T^2$ (m/s$^2$) |
| :---: | :---: | :---: | :---: |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| ... | | | |
| Mean | | | |

---

### 7. Results and Discussion

* High precision timing was achieved with optical interruption sensing.
* Calculated $g$ was close to expected value.
* Spread in period values was very small, suitable for studying non-ideal effects.

---

### 8. Precautions

1. Keep LED and phototransistor rigidly aligned.
2. Ensure pendulum motion is in one plane.
3. Measure effective length carefully.
4. Keep external light reflections minimal.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No pulse at SEN | Misalignment or wrong wiring | Re-align optical path and check pins |
| Highly noisy timing | Ambient light fluctuations | Shield detector from room light |
| Large spread in $T$ | Pendulum wobble/twist | Reduce amplitude and improve mounting |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why use light barrier instead of stopwatch?</b></summary><p><b>Ans:</b> It removes human reaction error and gives microsecond-level precision.</p></details>
<details><summary><b>Q2. Why does large amplitude alter period?</b></summary><p><b>Ans:</b> Small-angle approximation fails at large angles, increasing period slightly.</p></details>
</div>

