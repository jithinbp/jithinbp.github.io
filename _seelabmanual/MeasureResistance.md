---
layout: manual
title: "Measuring Resistance using SEN"
date: 28 April 2026
section: Getting Started
image:
  path: /assets/img/seelab/GetStart/images/measureRES-screen-phone.jpg
caption: Measuring resistances using the SEN Input
---

## Measuring Resistance

### 1. Aim

To measure an unknown resistance connected between `SEN` and `GND` using SEELab/ExpEYES.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Resistors (typical range: 100 ohm to 100 kohm)
* Connecting wires
* PC/Laptop/Android phone with SEELab software

### 3. Theory & Principle

Inside ExpEYES, `SEN` is connected to `3.3V` through an internal `5.1 kohm` resistor.
When an unknown resistor `R` is connected from `SEN` to `GND`, a voltage divider is formed.

$$
V_{SEN}=3.3\cdot\frac{R}{R+5100}
$$

Hence,
$$
R=5100\cdot\frac{V_{SEN}}{3.3-V_{SEN}}
$$

Best accuracy is obtained when `R` is of the same order as `5.1 kohm`.

### 4. Circuit Diagram / Setup

1. Connect one terminal of unknown resistor to `SEN`.
2. Connect other terminal to `GND`.
3. Open "Measure Resistance" in software/app.

### 5. Procedure

1. Start with a known resistor (for example `1 kohm`) for verification.
2. Note displayed resistance.
3. Repeat for `470 ohm`, `2.2 kohm`, `10 kohm`, `47 kohm`.
4. Compare measured and nominal values.
5. For unknown resistor, repeat measurement 3 times and average.

### 6. Observation Table

| Nominal Resistance | Measured Resistance | % Error | Remarks |
| :--- | :--- | :---: | :--- |
| 470 ohm | | | |
| 1 kohm | | | |
| 2.2 kohm | | | |
| 10 kohm | | | |
| 47 kohm | | | |

### 7. Series and Parallel Combinations

Use two known resistors (example: `R1 = 1 kohm`, `R2 = 2.2 kohm`) and verify equivalent resistance.

For series:
$$
R_{series}=R_1+R_2
$$

For parallel:
$$
R_{parallel}=\frac{R_1R_2}{R_1+R_2}
$$

Procedure:
1. Measure `R1` and `R2` individually.
2. Connect `R1` and `R2` in series between `SEN` and `GND`, then measure.
3. Connect `R1` and `R2` in parallel between `SEN` and `GND`, then measure.
4. Compare measured equivalents with calculated values.

| Combination | Calculated Equivalent | Measured Equivalent | % Error |
| :--- | :--- | :--- | :---: |
| `R1` alone | | | |
| `R2` alone | | | |
| `R1 + R2` (series) | | | |
| `R1 || R2` (parallel) | | | |

### 8. Advanced: Manual Calculation from SEN Voltage

If software shows `V_SEN`, calculate `R` manually using:
$$
R=5100\cdot\frac{V_{SEN}}{3.3-V_{SEN}}
$$

Example: if `V_SEN = 1.65V`,
$$
R=5100\cdot\frac{1.65}{1.65}=5100\ \Omega
$$

### 9. Error Analysis

* Measurement is less accurate at very low (`<<100 ohm`) or very high (`>>100 kohm`) resistance.
* Lead/contact resistance affects low-value measurements.
* Internal resistor tolerance and ADC resolution introduce small errors.

### 10. Precautions

1. Keep resistor leads firm and clean.
2. Do not apply external voltage directly to `SEN` in this experiment.
3. Use dry fingers / insulated clips; finger touch may alter high values.

### 11. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Reads nearly 0 ohm | Short circuit in wiring | Recheck connections |
| Reads very high / overflow | Open circuit / loose lead | Tighten clips |
| Reading unstable | Poor contact | Clean terminals and reconnect |

<div class="viva-section nosplit">

<h3> 12. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why is resistance measured between SEN and GND?</b></summary>
<p><b>Ans:</b> Because SEN has a known internal resistor to 3.3V, making a divider with the unknown resistor to GND.</p>
</details>

<details>
<summary><b>Q2. Why is measurement most accurate near a few kohms?</b></summary>
<p><b>Ans:</b> Maximum sensitivity occurs when unknown resistance is comparable to the internal 5.1 kohm resistor.</p>
</details>

<details>
<summary><b>Q3. What is the approximate measurable range?</b></summary>
<p><b>Ans:</b> Roughly 100 ohm to 100 kohm for useful accuracy.</p>
</details>

</div>
