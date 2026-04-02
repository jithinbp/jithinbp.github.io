---
layout: manual
title: "RL Circuit Steady State Response"
date: 28 March 2026
image:
  path: /assets/img/seelab/electrical/images/rlsteady-setup-seelab3.jpg
caption: Studying the steady-state AC response of a series L-R circuit
section: Electrical Engineering
---

## Steady-State Response of a Series RL Circuit

### 1. Aim

To study the behavior of a series RL circuit under a sinusoidal (AC) voltage, and to measure the **voltage amplitudes** across each element and the **phase difference** between the applied voltage and the current.

---

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* One Inductor ($L = 10\text{ mH}$, with internal DC resistance $r \approx 20\text{ }\Omega$)
* One Resistor ($R = 1\text{ k}\Omega$)
* Connecting wires
* PC or Smartphone with SEELab3 / ExpEYES software

---

### 3. Theory & Principle

When a sinusoidal voltage $V(t) = V_0 \sin(\omega t)$ is applied to a series RL circuit, the inductor offers a frequency-dependent opposition called **Inductive Reactance**, given by:

$$Z_L = 2\pi f L$$

Unlike a resistor, an ideal inductor does not dissipate energy — it stores energy in its magnetic field. However, a real inductor also has a small **DC winding resistance** $r$ that must be included. The effective series resistance is therefore $R_{eff} = R + r$.

The **total impedance** of the series RL circuit is:

$$Z = \sqrt{R_{eff}^2 + Z_L^2}$$

The voltage across the inductor **leads** the current by $90°$ (i.e., $\frac{\pi}{2}$ radians). The **phase angle** between the applied voltage and the current (which is in phase with $V_R$) is:

$$\phi = \tan^{-1}\!\left(\frac{Z_L}{R_{eff}}\right)$$

Since the voltages across $R$ and $L$ are $90°$ out of phase, the total applied voltage is obtained by **phasor (vector) addition**:

$$V_{applied} = \sqrt{V_R^2 + V_L^2}$$

> **Note:** For $R = 1\text{ k}\Omega$ (+ $20\text{ }\Omega$ winding resistance), $L = 10\text{ mH}$, and $f = 5000\text{ Hz}$, the inductive reactance $Z_L = 2\pi \times 5000 \times 0.01 \approx 314\text{ }\Omega$. The calculated phase angle is $\phi = 17.12°$ and the measured value is approximately $18°$. The small discrepancy is due to component tolerances and the winding resistance of the inductor.

---

### 4. Circuit Diagram / Setup

1. **Series Connection:** Connect the Resistor ($R$) and Inductor ($L$) in series.
2. **AC Source:** Connect the free end of the inductor to **WG** (Wave Generator output of SEELab3/ExpEYES-17).
3. **Ground:** Connect the free end of the resistor to **GND**.
4. **Measurement (Applied Voltage):** Connect the **WG** end also to **A1** to monitor the applied sinusoidal voltage.
5. **Measurement (Resistor Voltage):** Connect the junction between $L$ and $R$ to **A2** to monitor $V_R$ (which is in phase with the current).

---

### 5. Procedure

1. Open the SEELab3 / ExpEYES app and select the **"RL Steady State"** experiment.
2. Set the wave generator (**WG**) to output a sinusoidal signal at **$f = 5000\text{ Hz}$**.
3. The oscilloscope screen will display **three traces**:
   * The **applied voltage** (from WG / A1)
   * The **voltage across R** ($V_R$, in phase with the current. A2.)
   * The **voltage across L** ($V_L$, leading the current by $90°$ . calculated as **A1-A2** )
4. Note the **peak amplitudes** of each trace from the display.
5. Observe the **phase difference** ($\phi$) between the applied voltage and $V_R$ as reported by the software.
6. Vary the frequency (e.g., 1000 Hz, 2000 Hz, 5000 Hz, 10000 Hz) and repeat Steps 3–5 to study how $Z_L$ and $\phi$ change with frequency.
7. Compare the **measured phase angle** and **voltages** with theoretically calculated values, remembering to include the winding resistance $r$ of the inductor.


<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rlsteady-screen-phone.jpg" alt="Distance Plot" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Steady State Response (Phone App)</p>
    </div>    
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rlsteady-setup-eyes17.png" alt="Falling Data" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Steady State Setup For ExpEYES17</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

**Resistor ($R$):** ________ $\Omega$ &emsp;|&emsp; **Inductor ($L$):** ________ mH &emsp;|&emsp; **Winding Resistance ($r$):** ________ $\Omega$

**Effective Resistance $R_{eff} = R + r$:** ________ $\Omega$

| Frequency $f$ (Hz) | $Z_L = 2\pi fL$ ($\Omega$) | Theoretical $\phi$ (°) | Measured $V_R$ (V) | Measured $V_L$ (V) | Measured $\phi$ (°) | $\sqrt{V_R^2 + V_L^2}$ (V) | Applied $V$ (V) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1000 | | | | | | | |
| 2000 | | | | | | | |
| 5000 | | | | | | | |
| 10000 | | | | | | | |
| 20000 | | | | | | | |

---

### 7. Results and Discussion

* The voltage across the inductor was observed to **lead** the current (and $V_R$) by approximately $90°$, which is opposite in sense to the RC circuit where $V_C$ lags.
* At $f = 5000\text{ Hz}$, the measured phase angle was found to be ________ °, against a theoretical value of $17.12°$.
* The vector sum $\sqrt{V_R^2 + V_L^2}$ was found to be ________ V, agreeing closely with the directly measured applied voltage of ________ V, verifying **Kirchhoff's Voltage Law** in phasor form.
* As frequency increases, $Z_L$ increases, causing the phase angle $\phi$ to increase and $V_L$ to dominate over $V_R$. This is the dual behavior of an RC circuit, where $Z_C$ decreases with frequency.

---

### 8. Precautions

1. **Include Winding Resistance:** A real inductor has a DC resistance $r$ in its winding. Always measure this with a multimeter and add it to $R$ when calculating the theoretical phase angle; ignoring it leads to a systematic error.
2. **Frequency Selection:** Choose a frequency where $Z_L$ is comparable to $R_{eff}$ to get a clearly observable phase difference. For $L = 10\text{ mH}$ and $R = 1\text{ k}\Omega$, this is around $f \approx \frac{R}{2\pi L} \approx 15.9\text{ kHz}$. Lower frequencies like $5000\text{ Hz}$ give a small but measurable phase angle.
3. **Core Saturation:** Do not use very large signal amplitudes with iron-core inductors, as the core may saturate, making the inductance non-linear and waveforms distorted.
4. **Stable Waveform:** Allow the waveform display to stabilize for a few seconds before recording amplitudes and phase differences.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **No phase shift visible; traces overlap** | Frequency too low — $Z_L \ll R$, so inductor is nearly a short circuit at DC-like frequencies. | Increase frequency significantly (try 5000 Hz or higher). |
| **Measured $\phi$ much larger than theoretical** | Winding resistance $r$ not accounted for in calculation. | Measure $r$ with a multimeter and use $R_{eff} = R + r$ in the formula. |
| **Waveforms are distorted / non-sinusoidal** | Iron-core inductor saturating at high signal levels. | Reduce the WG output amplitude, or use an air-core inductor. |
| **$V_L$ trace is flat or missing** | Loose connection at the inductor or wrong channel assignment. | Check all connections; verify channel assignments in the software. |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. What is inductive reactance and how does it differ from resistance?</b></summary>
<p>
<b>Ans:</b> Inductive reactance ($Z_L = 2\pi fL$) is the opposition offered by an inductor to alternating current. Unlike resistance, it is directly proportional to frequency — it increases as frequency increases. A pure inductor stores energy in a magnetic field and releases it without dissipation, whereas a resistor permanently converts electrical energy into heat.
</p>
</details>

<details>
<summary><b>Q2. Why does the voltage across an inductor lead the current by 90°?</b></summary>
<p>
<b>Ans:</b> The voltage across an inductor is proportional to the rate of change of current: $V_L = L\frac{dI}{dt}$. A sinusoidal current $I = I_0 \sin(\omega t)$ gives $V_L = LI_0\omega\cos(\omega t) = LI_0\omega\sin(\omega t + 90°)$. Therefore the voltage always leads the current by exactly $90°$ in a pure inductor.
</p>
</details>

<details>
<summary><b>Q3. How does the behavior of an RL circuit differ from an RC circuit as frequency increases?</b></summary>
<p>
<b>Ans:</b> In an RL circuit, inductive reactance $Z_L = 2\pi fL$ increases with frequency, so $V_L$ grows and the phase angle $\phi$ increases toward $90°$ at very high frequencies (the circuit becomes predominantly inductive). In an RC circuit, capacitive reactance $Z_C = \frac{1}{2\pi fC}$ decreases with frequency, so $V_C$ shrinks and the phase angle decreases toward $0°$ — the two circuits are duals of each other.
</p>
</details>

<details>
<summary><b>Q4. Why must the winding resistance of the inductor be included in calculations?</b></summary>
<p>
<b>Ans:</b> A real inductor is wound from a long length of thin wire, which has a measurable DC resistance $r$. This resistance is always in series with the inductive reactance. Ignoring it means using an incorrect value of effective resistance $R_{eff}$, which causes the theoretical phase angle to differ from the measured value, even when the component values are otherwise accurate.
</p>
</details>

<details>
<summary><b>Q5. At what frequency will the voltages across R and L be equal in a series RL circuit?</b></summary>
<p>
<b>Ans:</b> The voltages are equal when $V_R = V_L$, which occurs when $R_{eff} = Z_L$, i.e., $R_{eff} = 2\pi fL$. Solving: $f = \frac{R_{eff}}{2\pi L}$. For $R_{eff} = 1020\text{ }\Omega$ and $L = 10\text{ mH}$, this gives $f \approx \frac{1020}{2\pi \times 0.01} \approx 16.2\text{ kHz}$. At this frequency, the phase angle $\phi = 45°$.
</p>
</details>

</div>