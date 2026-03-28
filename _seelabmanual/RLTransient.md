---
layout: manual
title: "RL Circuit Transients"
date: 28 March 2026
image:
  path: /assets/img/seelab/electrical/images/rltransient-setup-eyes17.png
caption: Capturing the growth and decay of current in an RL circuit
section: Electrical Engineering
---

## Experiment: Transient Response of an RL Circuit

### 1. Aim

To study the transient behavior of an Inductor-Resistor (RL) circuit, observe the growth and decay of current, and determine the **Inductance ($L$)** by fitting the experimental data.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* One Resistor ($R = 100\text{ }\Omega$ or $1000\text{ }\Omega$)
* One Inductor (e.g., 3000-turn coil provided in the kit)
* Connecting wires
* PC or Smartphone with SEELab3 software

### 3. Theory & Principle

Unlike a capacitor which opposes changes in voltage, an **Inductor ($L$)** opposes changes in **current** ($I$). When a voltage step ($V_0$) is applied to a series RL circuit, the current does not reach its maximum value ($V_0/R$) instantaneously due to the induced back-EMF.

The current growth is described by:
$$I(t) = \frac{V_0}{R} (1 - e^{-t/\tau})$$



The voltage across the inductor ($V_L$) during this growth is:
$$V_L(t) = V_0 e^{-t/\tau}$$

The **Time Constant ($\tau$)** is defined as:
$$\tau = \frac{L}{R_{total}}$$
Where $R_{total}$ is the sum of the external resistor and the internal DC resistance of the inductor coil.

### 4. Circuit Diagram / Setup

1.  **Series Connection:** Connect the Resistor ($R$) and Inductor ($L$) in series.
2.  **Input Source:** Connect one end of the Resistor to **OD1** (Digital Output used for the voltage step).
3.  **Ground:** Connect one end of the Inductor to **GND**.
4.  **Measurement:** Connect the junction between the Resistor and Inductor to **A1**.
5.  **Note:** In this configuration, **A1** measures the voltage across the Inductor ($V_R$).



### 5. Procedure

1.  Open the SEELab3 software and select the **"RL Transient"** experiment.
2.  The software toggles **OD1** from $0V$ to $5V$ while capturing high-speed data at **A1**.
3.  Click **"Capture"**. You will see the current ($V_R$) rising exponentially toward a steady-state value.
4.  **Data Analysis:** Select the rising portion of the curve.
5.  Use the "Exponential Fit" tool. The software will calculate the time constant $\tau$.
6.  Measure the DC resistance of your coil ($R_L$) using the SEELab ohmmeter.
7.  Calculate Inductance: $L = \tau \times (R + R_L)$.





<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rltransient-schematic.png" alt="Distance Plot" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Schematic Diagram (A2 Optional)</p>
    </div>
    
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rltransient-screen-pc.png" alt="Falling Data" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Charging and Discharge Curves</p>
    </div>

  </div>
</div>

### 6. Observation Table

**External Resistor ($R$):** ________ $\Omega$ | **Coil Resistance ($R_L$):** ________ $\Omega$

| Trial | Measured Time Constant $\tau$ (ms) | Calculated Inductance $L$ (mH) |
| :--- | :--- | :--- |
| 1 | | |
| 2 | | |
| **Mean** | | |

### 7. Results and Discussion

* The current in the RL circuit increased exponentially, confirming the presence of a back-EMF in the inductor.
* The measured inductance was found to be ________ mH.
* If a different resistor ($R$) is used, the time constant $\tau$ ________ (increases/decreases), but the calculated $L$ should remain constant.

### 8. Python Programming & Data

This experiment utilizes high-speed triggering to capture the sub-millisecond transition of the inductor.

* [Download Python Program for RL Transient](https://expeyes.in/software/python/rl_transient.py)
* [Download Analysis Script](https://expeyes.in/software/python/rl_transient_analyse.py)
* [Download Sample Data](https://expeyes.in/data/rl_transient.dat)

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **Current jumps instantly** | Inductance is too small. | Use a coil with more turns or lower the resistance $R$. |
| **Noisy Waveform** | Poor connections. | Ensure the inductor leads are making firm contact with the jumper wires. |
| **Calculated $L$ is wrong** | $R_L$ not included. | You MUST add the inductor's internal resistance to the external $R$ in the formula. |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why does the current in an RL circuit not reach its maximum value instantly?</b></summary>
<p>
<b>Ans:</b> According to Lenz's Law, as current starts to flow, the changing magnetic field induces a back-EMF in the inductor that opposes the growth of the current.
</p>
</details>

<details>
<summary><b>Q2. What is the definition of the Time Constant ($\tau$) for an RL circuit?</b></summary>
<p>
<b>Ans:</b> It is the time taken for the current to reach approximately $63.2\%$ of its maximum steady-state value ($V/R$).
</p>
</details>

<details>
<summary><b>Q3. What is the effect of an iron core on the RL time constant?</b></summary>
<p>
<b>Ans:</b> An iron core increases the inductance ($L$). Since $\tau = L/R$, inserting an iron core will increase the time constant, making the current rise more slowly.
</p>
</details>

<details>
<summary><b>Q4. Why is the Inductor's DC resistance ($R_L$) important in this experiment?</b></summary>
<p>
<b>Ans:</b> Unlike an ideal capacitor, a real inductor is made of a long wire which has significant resistance. This resistance is in series with the external resistor and affects the total time constant of the circuit.
</p>
</details>

<details>
<summary><b>Q5. What happens to the inductor voltage at the exact moment the switch is closed ($t=0$)?</b></summary>
<p>
<b>Ans:</b> At $t=0$, the inductor acts as an open circuit (to oppose the infinite change in current). Therefore, the entire source voltage ($V_0$) appears across the inductor, and the voltage across the resistor is zero.
</p>
</details>

</div>