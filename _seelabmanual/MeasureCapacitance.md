---
layout: manual
title: "Measuring Capacitance using IN1"
date: 28 April 2026
section: Getting Started
video: NMeqCf7tGmQ
image:
  path: /assets/img/seelab/GetStart/images/measureCAP-setup-eyes17.jpg
caption: Measuring capacitances using the IN1 Input, and making your own capacitors
---

## Measuring Capacitance

### 1. Aim

To measure capacitance connected between `IN1` and `GND`, and study how geometry affects capacitance.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Capacitors of known values
* Connecting wires / crocodile clips
* Two foil plates + paper/plastic sheet (for homemade capacitor)
* PC/Laptop/Android phone with SEELab software

### 3. Theory & Principle

Capacitance is defined as:
$$
C=\frac{Q}{V}
$$

SEElab measures small capacitances (pF and nF ranges) by charging with a constant current source and measuring the voltage rise produced. Q is the product of C and V, and Q can be calculated as a product of this constant current and the time spent charging.
For a parallel-plate capacitor:
$$
C\propto\frac{A}{d}
$$
More explicitly (same dielectric):
$$
C = \epsilon \frac{A}{d}
$$
where `A` is plate overlap area and `d` is separation.

For larger values, it charges the capacitor via a built-in 10K resistor whilst simultaneously capturing the capacitor voltage using the oscilloscope. All this magic happens internally, and the capacitance value is extracted after fitting the charging curve to an appropriate function to extract the time constant.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 38%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/GetStart/images/measureCAP-screen-phone.jpg" alt=" Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Mobile App</p>
    </div>
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/GetStart/images/cap-on-A1-setup-eyes17.jpg" alt=" Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Photo with ExpEYES17</p>
    </div>
  </div>
</div>



### 4. Circuit Diagram / Setup

1. Connect capacitor between `IN1` and `GND`.
2. Open the "Measure Capacitance" tool and trigger measurement.
3. Repeat with different capacitors.

### 5. Procedure

1. Measure known capacitors and record values.
2. Build a parallel-plate capacitor using foil-paper-foil.
3. Measure capacitance for full overlap.
4. Reduce overlap area gradually and re-measure.
5. Compare trends in measured values.

### 6. Observation Table

| Capacitor Type | Expected Value | Measured Value | Remarks |
| :--- | :--- | :--- | :--- |
| Ceramic (nominal) | | | |
| Electrolytic (nominal) | | | |
| Homemade plate capacitor (full area) | | | |
| Homemade plate capacitor (reduced area) | | | |

### 7. Advanced: Area Dependence Check

For same dielectric and separation:
$$
\frac{C_2}{C_1} \approx \frac{A_2}{A_1}
$$

Example: if overlap area is reduced to half, measured capacitance should be approximately half.

### 8. Error Analysis

* Stray capacitance of wires and surroundings affects small-capacitance readings.
* Touching plates with fingers adds parallel leakage paths and body capacitance.
* Poor clip contacts and unstable setup can cause fluctuations.

### 9. Precautions

1. Do not touch capacitor plates during measurement.
2. Keep leads short for pF-range measurements.
3. Ensure capacitor is discharged before reconnecting.
4. Use firm clips and avoid movement while reading.

### 10. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Reading too high | Stray/body capacitance | Keep hands away, shorten leads |
| Reading unstable | Loose connection/electrical noise | Tighten clips/remove nearby power cables |
| No reading | Wrong terminal | Ensure capacitor is between IN1 and GND |

### [Video Resource: https://www.youtube.com/embed/NMeqCf7tGmQ](https://www.youtube.com/embed/NMeqCf7tGmQ)

<div class="no-print"><iframe width="560" height="315" src="https://www.youtube.com/embed/NMeqCf7tGmQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>

<div class="viva-section nosplit">

<h3> 11. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why should you not touch capacitor plates while measuring?</b></summary>
<p><b>Ans:</b> Touch introduces leakage and extra capacitance, changing measured value.</p>
</details>

<details>
<summary><b>Q2. How does capacitance change with plate overlap area?</b></summary>
<p><b>Ans:</b> Capacitance is directly proportional to overlap area.</p>
</details>

<details>
<summary><b>Q3. What happens when plate separation increases?</b></summary>
<p><b>Ans:</b> Capacitance decreases because $C$ is inversely proportional to separation.</p>
</details>

</div>
