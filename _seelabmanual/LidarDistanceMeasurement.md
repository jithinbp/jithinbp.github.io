---
layout: manual
title: "Distance Measurement using LIDAR (VL53L0X)"
date: 31 March 2026
image:
  path: /assets/img/seelab/mechanics/images/lidar-setup-seelab3.jpg
caption: VL53L0X LIDAR measuring displacement of oscillating mass
section: Mechanics
---

## Distance Measurement using LIDAR

### 1. Aim

To measure distance as a function of time using VL53L0X and determine oscillation frequency of a mass-spring system.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* VL53L0X I2C LIDAR module
* Spring-mass setup (or fixed target for calibration)
* Connecting wires
* Data plotting/analysis tool

---

### 3. Theory & Principle

VL53L0X estimates distance by optical time-of-flight. Recording distance over time for periodic motion and fitting to:

$$x(t)=x_0 + A\sin(2\pi ft+\phi)$$

gives oscillation frequency $f$ and period $T=1/f$.

---

### 4. Circuit Diagram / Setup

1. Connect VL53L0X via I2C interface to SEELab3.
2. Verify reading with a static surface.
3. Mount sensor facing oscillating mass on spring.

---

### 5. Procedure

1. Acquire distance-time data for fixed target (baseline check).
2. Set spring-mass oscillation and record data.
3. Plot distance vs time.
4. Fit sinusoidal model and extract frequency.
5. Repeat for different masses if needed.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/lidar-screen1-phone.jpg" alt="LIDAR - Mobile Screen 1" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 1</p>
    </div>
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/mechanics/images/lidar-screen2-phone.jpg" alt="LIDAR - Mobile Screen 2" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Screen 2</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | Mass (g) | Mean distance (cm) | Frequency (Hz) | Period (s) |
| :---: | :---: | :---: | :---: | :---: |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

### 7. Results and Discussion

* LIDAR provided non-contact displacement measurement.
* Oscillation frequency was measured as ________ Hz for mass ________ g.
* Non-contact method reduces mechanical loading errors.

---

### 8. Precautions

1. Keep target reflectivity adequate and stable.
2. Avoid strong ambient IR interference.
3. Align sensor normal to target motion direction.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No distance output | I2C miswiring | Check SDA/SCL and power pins |
| Highly noisy signal | Bad alignment/reflectivity | Realign and use reflective surface |
| Incorrect fit | Non-sinusoidal motion | Reduce damping and use clean oscillation |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why use LIDAR for oscillation measurement?</b></summary><p><b>Ans:</b> It provides non-contact, high-resolution position sensing over time.</p></details>
<details><summary><b>Q2. How is frequency extracted from distance data?</b></summary><p><b>Ans:</b> By fitting the recorded waveform with a sinusoidal function and reading fitted frequency parameter.</p></details>
</div>

