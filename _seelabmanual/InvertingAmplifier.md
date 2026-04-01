---
layout: manual
title: "Inverting Amplifier using Op-Amp"
date: 31 March 2026
image:
  path: /assets/img/seelab/electronics/images/inv-amp-setup-seelab3.jpg
caption: OP07 inverting amplifier with Ri = 1 kOhm and Rf = 10 kOhm
section: Electronics
---

## Experiment: Inverting Amplifier using Op-Amp

### 1. Aim

To build an **inverting op-amp amplifier** using OP07, verify its voltage gain and phase inversion, and study output clipping when input amplitude is increased.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* OP07 single-channel op-amp
* Input resistor: $R_i = 1\text{ kOhm}$
* Feedback resistor: $R_f = 10\text{ kOhm}$
* Dual supply for op-amp: approximately $\pm 6\text{ V}$
* Breadboard and connecting wires
* PC/mobile with SEELab3 software

---

### 3. Theory & Principle

In an inverting amplifier, the non-inverting terminal is grounded, input is applied to the inverting terminal through $R_i$, and feedback is provided through $R_f$.

For ideal op-amp operation with negative feedback:

$$A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_i}$$

With $R_i = 1\text{ kOhm}$ and $R_f = 10\text{ kOhm}$:

$$A_v = -10$$

So the output should be:

* **10 times larger in amplitude** than input (within linear region),
* **180 degrees out of phase** (inverted).

If input is too large, required output exceeds supply rails and the op-amp saturates, producing clipping.

---

### 4. Circuit Diagram / Setup

1. Power OP07 with dual rails (about $+6\text{ V}$ and $-6\text{ V}$).
2. Connect **non-inverting input (+)** to GND.
3. Connect **$R_i = 1\text{ kOhm}$** from WG output to inverting input (-).
4. Connect **$R_f = 10\text{ kOhm}$** from op-amp output back to inverting input (-).
5. Measure:
   * input waveform at WG (or input node),
   * output waveform at op-amp output.
6. Set WG amplitude to around **80 mV** initially.

---

### 5. Procedure

1. Build the circuit and verify all power connections before applying input signal.
2. Set WG to a sine wave (for example 500 Hz to 1 kHz) with amplitude about **80 mV**.
3. Observe input and output simultaneously.
4. Record:
   * input peak-to-peak voltage $V_{in,pp}$,
   * output peak-to-peak voltage $V_{out,pp}$,
   * phase relation between input and output.
5. Compute gain:

$$A_v = \frac{V_{out,pp}}{V_{in,pp}}$$

6. Increase input amplitude gradually (e.g., up to around 1 V) and observe clipping.
7. Note the input level at which output first departs from a clean sine wave.

<img src="/assets/img/seelab/electronics/images/inv-amp-schematic.svg" style="width: 70%; display: block; margin: 20px auto; border: none;">

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/inv-amp-screen-phone.jpg" alt="Inverting Amplifier - Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Mobile App</p>
    </div>
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/inv-amp-screen-pc.png" alt="Inverting Amplifier - Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Desktop App</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | $V_{in,pp}$ (V) | $V_{out,pp}$ (V) | Calculated Gain $A_v$ | Phase shift | Waveform quality |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 (small signal) | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 (high input) | | | | | |

---

### 7. Results and Discussion

* The measured gain in the linear region was approximately ________, close to theoretical value of $-10$.
* Output waveform was inverted relative to input (approximately 180 degrees phase shift).
* At higher input amplitude, output clipped near the op-amp supply limits.
* The clipping confirms that closed-loop gain formula is valid only while the op-amp remains in linear operation.

---

### 8. Precautions

1. Confirm OP07 pin configuration before wiring.
2. Use correct dual supply polarity; wrong polarity can damage the op-amp.
3. Start with low input amplitude (around 80 mV) and increase gradually.
4. Keep all grounds common between SEELab3 and amplifier circuit.
5. Verify resistor values ($R_i$, $R_f$) to avoid incorrect gain.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No output signal | Missing supply rails or wrong pin connections | Check OP07 power pins and output pin wiring |
| Gain not close to 10 | Wrong resistor values or bad connection at inverting node | Recheck $R_i=1\text{ kOhm}$, $R_f=10\text{ kOhm}$ |
| Output not inverted | Probes connected to wrong nodes | Measure true input node and output node again |
| Severe clipping at low input | Supply rails too low or op-amp wiring error | Verify $\pm 6\text{ V}$ rails and feedback path |
| Noisy/distorted output | Floating ground or loose breadboard contacts | Tighten wiring and ensure common ground |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. Why is this amplifier called an inverting amplifier?</b></summary>
<p>
<b>Ans:</b> Because the output is 180 degrees out of phase with the input. A positive input excursion gives a negative output excursion and vice versa.
</p>
</details>

<details>
<summary><b>Q2. Derive gain for the inverting amplifier.</b></summary>
<p>
<b>Ans:</b> With ideal op-amp and negative feedback, input current into op-amp is approximately zero and the inverting node is virtual ground. So current through $R_i$ equals current through $R_f$:
$\frac{V_{in}}{R_i} = -\frac{V_{out}}{R_f}$. Therefore, $V_{out}/V_{in} = -R_f/R_i$.
</p>
</details>

<details>
<summary><b>Q3. Why does output clip at high input amplitude?</b></summary>
<p>
<b>Ans:</b> The op-amp output cannot exceed its supply rails. If required output from $A_v \cdot V_{in}$ is larger than available swing, the output saturates at rail limits, causing clipping.
</p>
</details>

<details>
<summary><b>Q4. What is a virtual ground in this circuit?</b></summary>
<p>
<b>Ans:</b> Due to high open-loop gain and negative feedback, the inverting input is held at nearly 0 V (same as non-inverting grounded input), though it is not directly connected to ground.
</p>
</details>

<details>
<summary><b>Q5. How can gain be increased without changing circuit topology?</b></summary>
<p>
<b>Ans:</b> Increase $R_f$ or decrease $R_i$, because $|A_v| = R_f/R_i$. However, larger gain reduces allowable input range before clipping.
</p>
</details>

</div>
