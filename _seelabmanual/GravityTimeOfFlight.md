---
layout: manual
title: "Gravity by Time of Flight"
date: 31 March 2026
image:
  path: /assets/img/seelab/mechanics/images/tof-setup-seelab3.jpg
caption: Steel ball release using electromagnet and contact sensor
section: Mechanics
---

## Determination of g by Time of Flight

### 1. Aim

To determine acceleration due to gravity by measuring time taken by a freely falling steel ball over a known distance.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* Electromagnet release assembly
* Mild steel ball
* Contact sensor plate
* Scale/ruler for measuring drop distance
* Python scripts (`tof.py`, `tof-analyse.py`)

---

### 3. Theory & Principle

For free fall from rest:

$$S=\frac{1}{2}gt^2 \quad \Rightarrow \quad g=\frac{2S}{t^2}$$

Measure drop height $S$ and time of flight $t$ to compute $g$.

Example from setup: $S=27\text{ cm}$ with $t\approx0.2354\text{ s}$ gives $g\approx974.5\text{ cm/s}^2$.

---

### 4. Circuit Diagram / Setup

1. Fix electromagnet at known height.
2. Place contact sensor directly below drop path.
3. Hold steel ball with electromagnet and release under software control.
4. Measure vertical distance from ball's lowest point to sensor.

---

### 5. Procedure

1. Measure $S$ accurately.
2. Perform one release and verify trigger timings.
3. Run repeated trials (50-100 readings recommended).
4. Save time data (`tof.csv`).
5. Compute $g$ for each reading.
6. Plot histogram and fit Gaussian for random error estimate.

<img src="/assets/img/seelab/mechanics/images/tof-screen-phone.jpg" style="width: 35%; display: block; margin: 20px auto;">

---

### 6. Observation Table

| Trial | $S$ (m) | $t$ (s) | $g=2S/t^2$ (m/s$^2$) |
| :---: | :---: | :---: | :---: |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| ... | | | |
| Mean | | | |

---

### 7. Results and Discussion

* Measured mean value of $g$ was ________ m/s$^2$.
* Distribution width indicated timing repeatability of ________.
* Systematic error can arise from delayed mechanical release after magnet de-energizing.

---

### 8. Precautions

1. Keep ball release point fixed for all trials.
2. Ensure sensor contact is reliable and noise-free.
3. Minimize lateral motion during release.
4. Use enough trials to separate random and systematic error.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Very high/low $g$ | Wrong distance reference | Re-measure $S$ from correct point |
| Large scatter in $t$ | Irregular release mechanics | Improve magnet-ball alignment |
| Missed impacts | Sensor contact issue | Recheck contact plate wiring |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why does delayed release affect measured g?</b></summary><p><b>Ans:</b> Timing starts before actual free fall if magnetic hold decays slowly, increasing measured $t$ and lowering calculated $g$.</p></details>
<details><summary><b>Q2. Why take many trials?</b></summary><p><b>Ans:</b> To estimate uncertainty and separate random fluctuations from systematic bias.</p></details>
</div>

