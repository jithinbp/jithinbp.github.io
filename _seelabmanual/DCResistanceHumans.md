---
layout: manual
title: "DC Resistance of Humans"
date: 27 March 2026
image:
  path: /assets/img/seelab/GetStart/images/dc-human-setup-seelab3.jpg
caption: Measure DC Resistance of the Body
section: Getting Started
---

## Measurement of DC Resistance of the Human Body

### 1. Aim

To measure the electrical resistance offered by the human body to a DC voltage using the SEELab3/ExpEYES toolkit and to observe how physical conditions like moisture and contact area affect this value.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 Test & Measurement Tool
* Set of connecting wires
* A PC, Laptop, or Android Phone with SEELab3 software installed
* Metal coins (optional, to test the effect of surface area)

### 3. Theory & Principle

The human body acts as a conductor, though it offers significant resistance primarily due to the dry outer layer of the skin (stratum corneum). In this experiment, the body is treated as a component in a **Potential Divider Network**.



The SEELab3 device has a known internal input impedance ($R_{in}$) at the **A2** terminal, typically $1\text{ M}\Omega$. When you connect your body between the voltage source (**PV1**) and the input terminal (**A2**), the voltage measured at A2 ($V_{A2}$) is determined by:

$$V_{A2} = V_{PV1} \times \frac{R_{in}}{R_{body} + R_{in}}$$

By measuring the voltage drop, the software calculates $R_{body}$ using Ohm's Law. For example, if your body offers exactly $1\text{ M}\Omega$ of resistance, the voltage at A2 will be exactly half of the voltage supplied by PV1.

### 4. Circuit Diagram / Setup

1.  Connect a wire from **PV1** to **A1** to monitor the source voltage.
2.  Connect a second wire to **PV1** and hold its metal tip firmly with your left hand.
3.  Connect a third wire to **A2** and hold it with your right hand.
4.  The circuit is completed through your chest and arms, flowing from **PV1** to **A2**.



### 5. Procedure

1.  Launch the SEELab3 software and navigate to the "DC Resistance of Human Body" experiment.
2.  Hold the bare end of the **PV1** wire in one hand and the **A2** wire in the other.
3.  Observe the resistance value displayed on the software interface.
4.  **Test for Surface Area:** Place a metal coin between your fingers and the wire tips to increase the contact area and note the change.
5.  **Test for Moisture:** Dampen your fingertips slightly with water and repeat the measurement.

<img src="/assets/img/seelab/GetStart/images/dc-human-screen-phone.jpg" style="width: 60%; display: block; margin: 0 auto;">

### 6. Observation Table

**Reference Impedance ($R_{in}$):** $1.0\text{ M}\Omega$

| Condition | Voltage at PV1 (V) | Voltage at A2 (V) | Measured Resistance ($M\Omega$) |
| :--- | :--- | :--- | :--- |
| Dry Hands (Finger Tip) | | | |
| Dry Hands (Holding Coins) | | | |
| Wet Hands | | | |

### 7. Error Analysis

* **Contact Pressure:** Variable pressure on the wire tips changes the effective contact area, leading to fluctuating resistance values.
* **Internal Impedance Tolerance:** The $1\text{ M}\Omega$ internal resistance of A2 may have a $\pm 1\%$ tolerance, which directly affects the calculated $R_{body}$.
* **Sweat and Electrolytes:** Natural salts on the skin can create a parallel conductive path, making the "dry" reading vary significantly between different individuals.

### 8. Results and Discussion

* The DC resistance of the human body was found to be approximately ________ $M\Omega$ under normal dry conditions.
* **Observation on Area:** Increasing the contact area using coins **decreased** the measured resistance. This follows the formula $R = \rho L/A$.
* **Observation on Moisture:** Wetting the hands **decreased** the resistance significantly, as water provides a much better conductive path through the skin's surface.

### 9. Precautions

1.  **Consistent Contact:** Ensure the wires make firm contact with the skin; loose contact will lead to erratic resistance calculations.
2.  **Voltage Safety:** Use only the low-voltage DC outputs (**PV1**) provided by the SEELab3. **Never connect the inputs to AC mains.**
3.  **Software Selection:** Ensure the correct hardware model is selected in the software settings so the internal $1\text{ M}\Omega$ impedance is correctly factored.

### 10. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **Resistance shows $\infty$** | Open circuit. | Ensure you are holding the metal tips of both wires firmly. |
| **Resistance shows $0\text{ }\Omega$** | Short circuit. | Ensure the PV1 and A2 wires are not touching each other. |
| **Unstable Readings** | Electrical noise. | Hold wires steadily; try running the laptop on battery power. |

<div class="viva-section nosplit">

<h3> 11. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why does wetting your hands decrease the measured resistance?</b></summary>
<p>
<b>Ans:</b> Dry skin is a poor conductor. Water (especially with dissolved skin salts) acts as an electrolyte that allows ions to move more freely, significantly increasing the conductivity and lowering the overall resistance.
</p>
</details>

<details>
<summary><b>Q2. In this experiment, what acts as the "Voltmeter" and what acts as the "Load"?</b></summary>
<p>
<b>Ans:</b> The <b>A2 terminal</b> (with its $1\text{ M}\Omega$ internal resistance) acts as the voltmeter, and the <b>human body</b> acts as the load resistor connected in series with it.
</p>
</details>

<details>
<summary><b>Q3. How does the path of the current change if you hold both wires in the same hand?</b></summary>
<p>
<b>Ans:</b> The current path becomes much shorter (just through the palm or fingers of one hand) rather than through the arms and chest. This will result in a much lower resistance reading.
</p>
</details>

<details>
<summary><b>Q4. Why do we use a high input impedance terminal like A2 for this measurement?</b></summary>
<p>
<b>Ans:</b> Since human body resistance is very high (often in the $M\Omega$ range), we need a measuring device with a comparable internal resistance ($1\text{ M}\Omega$) to create a measurable voltage drop in the potential divider.
</p>
</details>

<details>
<summary><b>Q5. Is the human body's resistance purely Ohmic (constant)?</b></summary>
<p>
<b>Ans:</b> No. Human resistance is non-linear and depends on voltage, frequency, and biological factors. High voltages can actually "break down" the skin's resistance, which is why high-voltage shocks are so dangerous.
</p>
</details>

</div>