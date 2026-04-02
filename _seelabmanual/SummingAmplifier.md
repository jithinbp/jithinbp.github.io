---
layout: manual
title: "Summing Amplifier using Op-Amp"
date: 31 March 2026
image:
  path: /assets/img/seelab/electronics/images/sum-amp-setup-seelab3.jpg
caption: OP07 summing amplifier with R1 = R2 = Rf = 1 kOhm
section: Electronics
---

## Summing Amplifier using Op-Amp

### 1. Aim

To build an inverting **summing amplifier** using OP07 and verify that output is proportional to the algebraic sum of input voltages.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* OP07 op-amp
* $R_1 = 1\text{ kOhm}$, $R_2 = 1\text{ kOhm}$, $R_f = 1\text{ kOhm}$
* Dual supply for op-amp (about $\pm 6\text{ V}$)
* Breadboard and connecting wires

---

### 3. Theory & Principle

For an inverting summing amplifier:

$$V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2}\right)$$

With $R_1 = R_2 = R_f$:

$$V_{out} = -(V_1 + V_2)$$

So for $V_1 = 1\text{ V}$ and $V_2 = 2\text{ V}$, expected output is:

$$V_{out} = -3\text{ V}$$

The same circuit can be tested with AC signals to observe real-time waveform addition and inversion.

---

### 4. Circuit Diagram / Setup

1. Power OP07 with dual supply.
2. Ground the non-inverting input (+).
3. Apply input $V_1$ (PV1) through $R_1$ to inverting node.
4. Apply input $V_2$ (PV2) through $R_2$ to the same inverting node.
5. Connect $R_f$ from output to inverting node.
6. Measure output using A1/scope.

---

### 5. Procedure

1. Set PV1 = 1 V and PV2 = 2 V.
2. Record output voltage and compare with theoretical -3 V.
3. Repeat for multiple input pairs.
4. Replace one or both DC inputs with AC signals and observe summed output.
5. Increase amplitude and note clipping near supply rails.

<img src="/assets/img/seelab/electronics/images/sum-amp-screen-phone.jpg" style="width: 35%; display: block; margin: 20px auto;">

---

### 6. Observation Table

| Trial | $V_1$ (V) | $V_2$ (V) | Expected $V_{out}$ (V) | Measured $V_{out}$ (V) | Error (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1.0 | 2.0 | -3.0 | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

### 7. Results and Discussion

* The circuit performed weighted addition with inversion.
* For equal resistors, measured output followed $V_{out} \approx -(V_1 + V_2)$.
* At larger input combinations, output clipping appeared near op-amp rail limits.

---

### 8. Precautions

1. Ensure common ground for all input sources and SEELab3.
2. Verify resistor values before power-on.
3. Start with low input levels to avoid clipping.
4. Check OP07 supply polarity and pinout.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Output incorrect sign | Wrong input connected to non-inverting path | Recheck inverting summing topology |
| Output not equal to sum | Wrong resistor values | Confirm $R_1$, $R_2$, $R_f$ values |
| Output clipped | Input sum too large | Reduce input amplitude/DC level |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. Why is summing amplifier output negative for positive inputs?</b></summary>
<p><b>Ans:</b> Because input signals are applied to the inverting terminal with negative feedback.</p>
</details>

<details>
<summary><b>Q2. How does unequal resistor choice change behavior?</b></summary>
<p><b>Ans:</b> Each input gets a different weight: $V_{out} = -R_f(V_1/R_1 + V_2/R_2)$.</p>
</details>

</div>
