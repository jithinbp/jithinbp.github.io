---
layout: manual
title: "LCR Circuit Transients"
date: 28 March 2026
image:
  path: /assets/img/seelab/electrical/images/rlctransient-setup-seelab3.jpg
caption: Observing damped oscillations in a series RLC circuit
section: Electrical Engineering
---

## Transient Response of an RLC Circuit

### 1. Aim

To study the evolution of voltage across a capacitor in a series LCR circuit in response to a voltage step and to analyze the resulting damped oscillations.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Resistor ($R = 100\text{ }\Omega$)
* Inductor ($L = 10\text{ mH}$)
* Capacitor ($C = 0.1\text{ }\mu F$)
* Connecting wires
* PC or Smartphone with SEELab3 software

### 3. Theory & Principle

A series LCR circuit is a **second-order system**. When a voltage step ($v_s$) is applied, the relationship between the components is governed by Kirchhoff’s Voltage Law (KVL):

$$L\frac{di(t)}{dt} + Ri(t) + v_c(t) = v_s$$

Substituting $i = C\frac{dv_c}{dt}$, we get the second-order differential equation:

$$\frac{d^2v_c(t)}{dt^2} + \frac{R}{L}\frac{dv_c(t)}{dt} + \frac{v_c(t)}{LC} = \frac{v_s}{LC}$$



The behavior of the system depends on the roots of the characteristic equation:
$$\alpha^2 + \frac{R}{L}\alpha + \frac{1}{LC} = 0$$

Depending on the values of $L$, $C$, and $R$, the response can be:
1.  **Underdamped:** $(R/2L)^2 < 1/LC$ (Oscillations that decay over time).
2.  **Critically Damped:** $(R/2L)^2 = 1/LC$ (Fastest return to steady state without oscillation).
3.  **Overdamped:** $(R/2L)^2 > 1/LC$ (Slow return to steady state without oscillation).

For the **underdamped** case (using the provided components), the solution is a damped sinusoid:
$$v(t) = e^{\beta t} [K \sin(\gamma t + \theta)]$$
Where $\beta = -R/2L$ is the damping factor and $\gamma = \sqrt{\frac{1}{LC} - (\frac{R}{2L})^2}$ is the angular frequency of oscillation.



### 4. Circuit Diagram / Setup

1.  Connect the Resistor ($R$), Inductor ($L$), and Capacitor ($C$) in series.
2.  Connect the free end of the Resistor to **OD1** (Digital Output).
3.  Connect the free end of the Capacitor to **GND**.
4.  Connect **A1** to the junction between the inductor and the Capacitor to measure $v_c(t)$.

### 5. Procedure

1.  Open the SEELab3 software and select the **"LCR Transient"** experiment.
2.  Click on **"Step OD1 0-5V"**. The software applies a $5V$ step and captures the high-speed voltage variation at **A1**.
3.  Observe the oscillating waveform. Note how the amplitude of the sine wave decreases over time.
4.  **Analysis:** Select the oscillating region on the graph.
5.  Use the "Damped Sine Fit" tool. The software will extract the frequency and the damping factor ($\beta$).
6.  **Export:** Save the data as a CSV file for further analysis in Python.
7.  Click on **"Step OD1 5-0V"**. The software applies a $5-0V$ step and captures the high-speed voltage variation at **A1**. Repeat steps 3 through 6 .


<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rlctransient-screen-phone.jpg" alt="Distance Plot" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Transient Response (Phone App)</p>
    </div>
    
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electrical/images/rlctransient-screen-pc.png" alt="Falling Data" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Charging and Discharge Curves</p>
    </div>

  </div>
</div>

### 6. Observation Table

**Components:** $L = 10\text{ mH}$, $C = 0.1\text{ }\mu F$, $R = 100\text{ }\Omega$

| Parameter | Theoretical Value | Measured Value (from Fit) |
| :--- | :--- | :--- |
| Frequency ($f$) | | |
| Damping Factor ($\beta$) | | |
| Damping Ratio ($\zeta$) | | |

### 7. Results and Discussion

* The circuit exhibited _____________________________________, as expected from the selected component values.
* The frequency of oscillation was found to be ________ Hz.
* Increasing the resistance $R$ _____________ (increases/decreases) the damping, causing the oscillations to die out__________ (faster/slower).

### 8. Python Programming & Data

* [Download Python Program for LCR Transient](https://expeyes.in/software/python/lcr_transient.py)
* [Download Analysis Script](https://expeyes.in/software/python/lcr_analyse.py) (Rename exported file to `lcr.csv`)
* [Download Sample Data](https://expeyes.in/data/lcr_sample.csv)

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **No oscillations (Flat line)** | $R$ is too high (Overdamped). | Reduce $R$ to $100\text{ }\Omega$ or less. |
| **Frequency is very high** | $L$ or $C$ values are too small. | Ensure you are using $10\text{ mH}$ and $0.1\text{ }\mu F$. |
| **Fitting fails** | Not enough cycles captured. | Adjust the timebase to capture at least 3-5 full oscillations. |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. What determines whether an LCR circuit oscillates or not?</b></summary>
<p>
<b>Ans:</b> The relationship between the energy-storing components ($L, C$) and the energy-dissipating component ($R$). If the resistance is low enough ($R < 2\sqrt{L/C}$), the circuit will oscillate (As seen in the app screenshots).
</p>
</details>

<details>
<summary><b>Q2. What is the physical meaning of the damping factor $\beta$?</b></summary>
<p>
<b>Ans:</b> It represents the rate at which energy is lost from the circuit (as heat in the resistor). A larger $\beta$ means the amplitude of oscillations decays more rapidly.
</p>
</details>

<details>
<summary><b>Q3. What is the difference between "Natural Frequency" and "Damped Frequency"?</b></summary>
<p>
<b>Ans:</b> The natural frequency ($\omega_0 = 1/\sqrt{LC}$) is the frequency at which the circuit would oscillate if there were zero resistance. The damped frequency ($\gamma$) is always slightly lower than the natural frequency because of the resistance.
</p>
</details>

<details>
<summary><b>Q4. Why does the voltage across the capacitor eventually settle at 5V?</b></summary>
<p>
<b>Ans:</b> After the transients die out, the inductor acts as a short circuit and the capacitor acts as an open circuit to DC. Therefore, the entire source voltage ($v_s = 5V$) eventually appears across the capacitor.
</p>
</details>

<details>
<summary><b>Q5. What is "Critical Damping" used for in real-world applications?</b></summary>
<p>
<b>Ans:</b> Critical damping is used in systems where you want the output to reach the target value as quickly as possible without any "overshoot" or ringing, such as in analog voltmeter needles or car suspension systems.
</p>
</details>

</div>