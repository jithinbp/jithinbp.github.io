---
layout: manual
title: "Single Transistor Amplifier (Common-Emitter)"
date: 31 March 2026
image:
  path: /assets/img/seelab/electronics/images/tr-amp-setup-seelab3.jpg
caption: Single-stage NPN common-emitter amplifier using AC coupling at the base
section: Electronics
---

## Experiment: Single Transistor Amplifier

### 1. Aim

To build and test a **single-stage common-emitter transistor amplifier**, measure its input/output waveforms, and observe how bias point and input amplitude affect gain and distortion.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* NPN transistor (recommended: **2N2222**)
* Bias resistor: **100 kOhm** (base bias from PV2)
* Signal divider resistors: **1 kOhm** and **2.2 kOhm** (to attenuate WG signal)
* Coupling capacitor for base input (AC coupling)
* Collector and emitter resistors as per your standard amplifier setup
* Breadboard and connecting wires
* PC / mobile running SEELab3 interface

---


<img src="/assets/img/seelab/electronics/images/tr-amp-schematic.svg" style="width: 40%; display: block; margin: 20px auto; border: none;">

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/tr-amp-screen-phone.jpg" alt="Transistor Amplifier - Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Mobile App</p>
    </div>
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/tr-amp-screen-pc.png" alt="Transistor Amplifier - Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Desktop App</p>
    </div>
  </div>
</div>


### 3. Theory & Principle



This experiment uses a **common-emitter (CE) transistor amplifier**. The input AC signal is applied to the base through a coupling capacitor so that the DC bias condition is not disturbed.

Because CE gain can be high, a small input signal is needed to avoid clipping. The ExpEYES method uses a **1 kOhm : 2.2 kOhm divider** to reduce the waveform-generator signal to around a few tens of millivolts at the base input.

The transistor operating point (Q-point) is set by base bias through a **100 kOhm** resistor, controlled by **PV2**:

* If bias is too low -> cut-off during part of the cycle (bottom clipping).
* If bias is too high -> saturation during part of the cycle (top clipping).
* At proper bias -> maximum undistorted output swing.

#### Why small input is important

For linear amplification, the transistor must stay in active region over the signal cycle. If input amplitude is too high, the instantaneous operating point enters cut-off/saturation, causing waveform distortion.

---

### 4. Circuit Diagram / Setup

1. Build the CE amplifier wiring as in the output-characteristics style circuit (collector resistor, emitter to ground path, base bias through 100 kOhm).
2. Connect **WG** output to a divider network using **1 kOhm** and **2.2 kOhm**.
3. Feed the attenuated signal to the transistor base through a **coupling capacitor**.
4. Monitor:
   * **A2** -> input signal at base side (after divider/coupling).
   * **A1** -> output signal at collector.
5. Use **PV2** to adjust base bias for minimum distortion.

#### SEELab3 note

SEELab3 allows reducing WGbar amplitude using an external gain resistor. A **100 Ohm** resistor can reduce approximately 3 V to around 30 mV, suitable for low-distortion transistor amplification.

---

### 5. Procedure

1. Power the setup and open the relevant transistor amplifier tool/scope view in SEELab3.
2. Start with a low-frequency sine input (for example, 500 Hz to 1 kHz).
3. Keep input amplitude small using the divider (or WGbar attenuation method).
4. Observe input on A2 and output on A1.
5. Slowly vary **PV2**:
   * find a bias point where output is centered and least distorted.
6. Increase input amplitude gradually and note onset of clipping.
7. Record waveforms and estimate voltage gain:

$$A_v = \frac{V_{out,pp}}{V_{in,pp}}$$

8. Try these improvements and compare:
   * lower input amplitude,
   * higher collector supply (if external safe supply is used),
   * lower-gain transistor.


---

### 6. Observation Table

| Trial | $V_{in,pp}$ (mV) | $V_{out,pp}$ (V) | Bias setting (PV2) | Gain $A_v$ | Distortion observed |
| :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

### 7. Results and Discussion

* The CE stage produced an amplified output with phase inversion (approximately 180 degrees) relative to input.
* Best amplification occurred at an intermediate base bias where clipping was minimal.
* At low bias the output showed cut-off clipping; at high bias it showed saturation clipping.
* Measured voltage gain was $A_v =$ ________ under near-linear conditions.

---

### 8. Precautions

1. Keep input small; CE stages distort quickly for large base drive.
2. Always use coupling capacitor at base input to prevent bias shift by WG DC component.
3. Verify transistor pinout before powering the circuit.
4. Do not exceed safe collector current or device power limits.
5. Ensure common ground between SEELab3 and the circuit.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No output on A1 | Wrong transistor pinout / open collector path | Recheck E-B-C pin connections and resistor wiring |
| Output heavily clipped even at low input | Bias point too low/high | Adjust PV2 for centered undistorted waveform |
| Input appears too large | Divider not connected correctly | Verify 1 kOhm and 2.2 kOhm divider wiring |
| DC shift at base input | Missing/incorrect coupling capacitor | Replace/add base coupling capacitor |
| Very low gain | Transistor damaged or wrong resistor values | Check component values and swap transistor |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. Why is a coupling capacitor used at the transistor base?</b></summary>
<p>
<b>Ans:</b> The capacitor passes AC signal and blocks DC. This allows the signal to be superimposed on the chosen DC bias point without disturbing the base bias network.
</p>
</details>

<details>
<summary><b>Q2. Why does distortion occur if bias is not set correctly?</b></summary>
<p>
<b>Ans:</b> If the Q-point is too near cut-off or saturation, part of the input cycle drives the transistor out of active region. The output then clips, producing nonlinear distortion.
</p>
</details>

<details>
<summary><b>Q3. Why is input attenuated before feeding the base?</b></summary>
<p>
<b>Ans:</b> CE voltage gain can be high. A large input overdrives the transistor, so attenuating input to tens of millivolts keeps operation in the linear region.
</p>
</details>

<details>
<summary><b>Q4. What is the phase relation between input and output in CE amplifier?</b></summary>
<p>
<b>Ans:</b> The output at collector is inverted with respect to input by about 180 degrees.
</p>
</details>

<details>
<summary><b>Q5. Name three ways to reduce distortion in this experiment.</b></summary>
<p>
<b>Ans:</b> Reduce input amplitude, choose a better bias point (PV2 adjustment), and use a higher collector supply (within safe limits) or a transistor with lower gain.
</p>
</details>

</div>
