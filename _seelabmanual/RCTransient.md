---
layout: manual
title: "RC Circuit Transients"
date: 28 March 2026
image:
  path: /assets/img/seelab/electrical/images/rctransient-setup-seelab3.jpg
caption: Capturing the charging and discharging curves of an RC circuit
section: Electrical Engineering
---

## Experiment: Transient Response of an RC Circuit

### 1. Aim

To study the charging and discharging behavior of a capacitor in a series RC circuit and to determine the **Time Constant ($\tau$)** by fitting the experimental data.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* One Resistor ($R = 1\text{ k}\Omega$ )
* One Capacitor ($C = 1\text{ }\mu F$ )
* Connecting wires
* PC or Smartphone with SEELab3 software

### 3. Theory & Principle

When a voltage step ($V_0$) is applied to an empty capacitor through a resistor, the voltage across the capacitor ($V_C$) does not jump instantly. It increases exponentially according to:
$$V_C(t) = V_0(1 - e^{-t/RC})$$

Similarly, when a charged capacitor is allowed to discharge through a resistor, the voltage decays as:
$$V_C(t) = V_0 e^{-t/RC}$$



The product **$RC$** is called the **Time Constant ($\tau$)**. It represents the time required for the capacitor to charge to approximately $63.2\%$ of the applied voltage or discharge to $36.8\%$ of its initial value.

### 4. Circuit Diagram / Setup

1.  **Series Connection:** Connect the Resistor ($R$) and Capacitor ($C$) in series.
2.  **Input Source:** Connect the free end of the resistor to **OD1** (Digital Output used for the voltage step).
3.  **Ground:** Connect the free end of the capacitor to **GND**.
4.  **Measurement:** Connect the junction between the resistor and capacitor to **A1** to monitor $V_C$.



### 5. Procedure

1.  Open the SEELab3 app and select the **"RC Transient"** experiment.
2.  The software is programmed to toggle **OD1** from $0V$ to $5V$ and simultaneously start high-speed data acquisition on **A1**.
3.  Click on **"Charge"** (or Start). The software will apply the step and display the rising exponential curve.
4.  Click on **"Discharge"**. The software will set **OD1** to $0V$ and capture the falling exponential curve.
5.  **Data Fitting:** Select a region of the captured curve. Use the "Fit" tool to apply an exponential fit. The software will display the value of the time constant ($RC$).
6.  Compare the experimental $RC$ value with the theoretical value calculated from the component markings ($R \times C$).

<img src="/assets/img/seelab/electrical/images/rctransient-screen-phone.jpg" style="width: 50%; display: block; margin: 0 auto;">

<img src="/assets/img/seelab/electrical/images/rctransient-screen-pc.png" style="width: 70%; display: block; margin: 0 auto;">

### 6. Observation Table

**Resistor ($R$):** ________ $\Omega$ | **Capacitor ($C$):** ________ $\mu F$

| Process | Theoretical $\tau = RC$ (ms) | Measured $\tau$ from Fit (ms) | % Error |
| :--- | :--- | :--- | :--- |
| Charging | | | |
| Discharging | | | |

### 7. Results and Discussion

* The voltage across the capacitor followed an exponential path during both charging and discharging phases.
* The measured time constant was found to be ________ ms.
* The results verify that it takes approximately $5\tau$ for the capacitor to reach its steady-state (fully charged or discharged) condition.

### 8. Precautions

1.  **Selection of RC:** Choose $R$ and $C$ values such that the time constant is between $1\text{ ms}$ and $100\text{ ms}$. If $\tau$ is too small, the software may not have enough sampling resolution to capture the curve accurately.
2.  **Input Impedance:** The $1\text{ M}\Omega$ input impedance of **A1** is in parallel with the capacitor during discharge. For very high $R$ values (e.g., $1\text{ M}\Omega$), this will introduce significant error.
3.  **Residual Charge:** Ensure the capacitor is fully discharged before starting a new "Charge" cycle for a clean plot starting from $0V$.

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **Graph is a vertical line** | $\tau$ is too small. | Increase $R$ or $C$ value to slow down the process. |
| **Graph is a flat line at 0V** | OD1 not connected. | Check the connection between OD1 and the resistor. |
| **Fitting fails/gives error** | Noise in data. | Ensure connections are tight; select a cleaner portion of the curve for fitting. |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. What is the definition of the Time Constant ($\tau$) in an RC circuit?</b></summary>
<p>
<b>Ans:</b> It is the time taken by the capacitor to charge to approximately $63\%$ of its maximum voltage or to discharge to $37\%$ of its initial voltage.
</p>
</details>

<details>
<summary><b>Q2. How long does it take for a capacitor to be considered "fully" charged?</b></summary>
<p>
<b>Ans:</b> Theoretically, it takes infinite time. However, in practical engineering, a capacitor is considered fully charged after a time interval of $5\tau$, at which point it reaches $>99\%$ of the applied voltage.
</p>
</details>

<details>
<summary><b>Q3. If you double the resistance in a series RC circuit, what happens to the charging time?</b></summary>
<p>
<b>Ans:</b> Since $\tau = RC$, doubling the resistance doubles the time constant, meaning the capacitor will take twice as long to charge.
</p>
</details>

<details>
<summary><b>Q4. Why does the current in the circuit decrease as the capacitor charges?</b></summary>
<p>
<b>Ans:</b> As the capacitor charges, it develops an EMF that approaches the source voltage. The net voltage across the resistor ($V_0 - V_C$) decreases, and according to Ohm's Law ($I = V_R/R$), the current also decreases.
</p>
</details>

<details>
<summary><b>Q5. What is the initial current ($t=0$) when charging a capacitor?</b></summary>
<p>
<b>Ans:</b> At $t=0$, the capacitor acts like a short circuit ($V_C = 0$). Therefore, the initial current is maximum and is equal to $V_0/R$.
</p>
</details>

</div>