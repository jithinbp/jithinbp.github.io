---
layout: manual
title: "Study of Light Dependent Resistor (LDR)"
date: 28 April 2026
section: Getting Started
image:
  path: /assets/img/seelab/GetStart/images/ldr-setup-seelab3.jpg
caption: Study of Light Dependent Resistors(LDRs)
---

## Study of Light Dependent Resistor (LDR)

### 1. Aim

To study variation of LDR resistance with light intensity using `SEN` and `GND`.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* LDR
* Connecting wires
* Light source (phone torch / LED lamp)
* PC/Laptop/Android phone with SEELab software

### 3. Theory & Principle

LDR resistance decreases when light intensity increases.

In this experiment, LDR is connected between `SEN` and `GND`. Internally, `SEN` is connected to `3.3V` through `5.1 kohm`.
From measured `V_SEN`, LDR resistance is:
$$
R_{LDR}=5100\cdot\frac{V_{SEN}}{3.3-V_{SEN}}
$$

Lower light -> higher `R_LDR` -> higher `V_SEN` trend depends on divider orientation; verify experimentally.

### 4. Circuit Diagram / Setup

1. Connect LDR between `SEN` and `GND`.
2. Open resistance/LDR measurement screen in software.
3. Ensure ambient light condition is stable before taking readings.


<img src="/assets/img/seelab/GetStart/images/ldr-screen-phone.jpg" alt=" Mobile App" style="width: 60%; height: auto; border: 1px solid #eee;">

### 5. Procedure

1. Record reading in room light.
2. Increase light on LDR (torch close to LDR) and record reading.
3. Reduce light (cover partly or move source away) and record reading.
4. Repeat for multiple light levels.
5. Plot `R_LDR` vs relative light level (low/medium/high) or lux (if lux meter is available).

### 6. Observation Table

| Light Condition | Measured $V_{SEN}$ | Calculated / Displayed $R_{LDR}$ | Remarks |
| :--- | :--- | :--- | :--- |
| Dark / covered | | | |
| Room light | | | |
| Bright lamp | | | |
| Torch very close | | | |

### 7. Advanced: Sensitivity Estimation

Estimate change ratio:
$$
\text{Sensitivity ratio}=\frac{R_{\text{dark}}}{R_{\text{bright}}}
$$

Larger ratio indicates better light sensitivity.

If multiple points are taken, a log plot (`\log R` vs `\log L`) can be used to estimate empirical exponent:
$$
R\propto L^{-k}
$$

### 8. Error Analysis

* Ambient light fluctuations cause drift.
* Sensor heating or light-source flicker changes reading.
* Shadows and angle of incidence affect effective illumination.

### 9. Precautions

1. Keep light source distance fixed for repeated trials.
2. Avoid hand shadow while recording.
3. Wait 1-2 seconds after changing light before reading.
4. Do not apply external voltage directly to `SEN`.

### 10. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No variation in reading | Wrong wiring / faulty LDR | Recheck LDR between SEN and GND |
| Reading very noisy | Flickering light source | Use steady DC light source |
| Saturated high/low value | Too dark / too bright constantly | Adjust illumination range |

<div class="viva-section nosplit">

<h3> 11. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. What happens to LDR resistance when light increases?</b></summary>
<p><b>Ans:</b> LDR resistance decreases as light intensity increases.</p>
</details>

<details>
<summary><b>Q2. Why is SEN used in this experiment?</b></summary>
<p><b>Ans:</b> SEN has a known internal resistor to 3.3V, allowing resistance estimation from measured voltage.</p>
</details>

<details>
<summary><b>Q3. Why can two readings differ even at same lamp brightness?</b></summary>
<p><b>Ans:</b> Distance/angle changes, ambient light, and LDR response time can alter readings.</p>
</details>

</div>
