---
layout: manual
title: "Study of an Electromagnet"
date: 27 March 2026
image:
  path: /assets/img/seelab/school-level/images/emag-setup-seelab3.jpg
caption: Studying the magnetic field produced by a current-carrying coil
section: School Level Physics
---

## Study of an Electromagnet

### 1. Aim

To demonstrate that a current-carrying conductor produces a magnetic field and to study the properties of an electromagnet using a solenoid coil and a permanent magnet.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Solenoid coil (e.g., 3000 turns of SWG44 wire included in the kit)
* Small permanent bar magnet or a Compass
* Connecting wires
* PC or Smartphone with SEELab3 software

### 3. Theory & Principle

When an electric current ($I$) flows through a conductor, it creates a magnetic field around it (Oersted's discovery). A **Solenoid** is a long coil of wire consisting of many loops. When current passes through it, the magnetic fields of the individual loops add together to create a strong, uniform magnetic field inside the coil, behaving like a bar magnet.

The magnetic field strength ($B$) at the center of a long solenoid is given by:
$$B = \mu_0 \cdot n \cdot I$$

Where:
- $B$ is the magnetic flux density in Tesla ($T$).
- $\mu_0$ is the permeability of free space ($4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$).
- $n$ is the number of turns per unit length ($N/L$).
- $I$ is the current in Amperes ($A$).

**Current Limitation:**
The Programmable Voltage source (**PV1**) on SEELab3/ExpEYES has a **maximum current limit of 30mA**. 
- The standard coil provided (3000 turns) has a resistance ($R$) of approximately $500\text{ }\Omega$.
- At $5V$, the current drawn is $I = V/R = 5/500 = 10\text{ mA}$, which is well within the limit.

### 4. Circuit Diagram / Setup

1.  Connect one end of the solenoid coil to **PV1** and the other end to **GND**.
2.  Connect **PV1** to **A1** using a wire to monitor the actual voltage applied across the coil.
3.  Place a small permanent magnet or a compass needle near one end of the coil, aligned with its axis.

### 5. Procedure

1.  Open the SEELab3 software and select the "Electromagnet" or "Power Supply" tool.
2.  Set the voltage at **PV1** to $0V$.
3.  Slowly increase the voltage to $+5V$ and observe the movement of the magnet (Attraction or Repulsion).
4.  Change the voltage to $-5V$ (reverse polarity) and observe how the magnetic poles of the coil flip, causing the opposite force on the permanent magnet.
5.  **AC Study:** Set the Waveform Generator (**WG**) to a low frequency (e.g., $5\text{ Hz}$) and connect it to the coil to see the magnet vibrate as the poles oscillate.

<img src="/assets/img/seelab/school-level/images/emag-screen-phone.jpg" style="width: 60%; display: block; margin: 0 auto;">

### 6. Observation Table

**Coil Resistance ($R$):** ________ $\Omega$

| Set Voltage (V) | Measured Voltage A1 (V) | Current $I \approx V_{A1}/R$ (mA) | Observation (Attract/Repulse) |
| :--- | :--- | :--- | :--- |
| +5.0 | | | |
| +2.5 | | | |
| -2.5 | | | |
| -5.0 | | | |

### 7. Error Analysis

* **Voltage Drop:** If the measured voltage at **A1** is lower than the set **PV1** value, it indicates that the coil resistance is too low, hitting the $30\text{ mA}$ safety limit of the device.
* **Ambient Fields:** Nearby electronic devices or large metal objects can distort the magnetic field, affecting the compass needle or magnet movement.
* **Thermal Drift:** As the coil carries current, it heats up, which slightly increases its resistance ($R = R_0[1 + \alpha\Delta T]$), thereby decreasing the current and the magnetic field strength over time. Although this effect will not present itself for such low currents.

### 8. Results and Discussion

* The coil behaves as a magnet when current flows through it, confirming the magnetic effect of electric current.
* Reversing the direction of the current reverses the **polarity** of the electromagnet.
* The strength of the electromagnet is directly proportional to the magnitude of the current flowing through it.

### 9. Precautions

1.  **Current Limit:** Do not use coils with resistance less than $170\text{ }\Omega$ at $5V$ to avoid overloading the source.
2.  **Heat:** Do not leave the current running through the coil for extended periods.
3.  **Interference:** Keep sensitive electronic devices away from the strong magnetic field.

### 10. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **No magnetic force** | Broken coil wire. | Check continuity using the SEELab ohmmeter. |
| **Voltage A1 < Set PV1** | Current limit reached. | Use a higher resistance coil or lower the voltage. |
| **Magnet doesn't move** | Magnet is too far. | Move the magnet closer to the center of the coil. |

<div class="viva-section nosplit">

<h3> 11. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. What happens to the magnetic field if you insert an iron core into the solenoid?</b></summary>
<p>
<b>Ans:</b> The magnetic field strength increases significantly. Iron has a high magnetic permeability, which concentrates the magnetic flux lines, making the electromagnet much stronger.
</p>
</details>

<details>
<summary><b>Q2. How can you determine the North and South poles of an electromagnet?</b></summary>
<p>
<b>Ans:</b> You can use the <b>Right-Hand Thumb Rule</b>: Curl your fingers in the direction of the current flow; your thumb will point toward the North pole. Alternatively, use a magnetic compass.
</p>
</details>

<details>
<summary><b>Q3. Why does the magnet vibrate when the coil is connected to the Waveform Generator (WG)?</b></summary>
<p>
<b>Ans:</b> The WG provides Alternating Current (AC), which reverses direction periodically. This causes the poles of the electromagnet to flip back and forth, alternating between attracting and repelling the permanent magnet.
</p>
</details>

<details>
<summary><b>Q4. On what factors does the strength of an electromagnet depend?</b></summary>
<p>
<b>Ans:</b> It depends on the number of turns in the coil ($N$), the magnitude of the current ($I$), and the permeability of the core material ($\mu$).
</p>
</details>

<details>
<summary><b>Q5. Is an electromagnet a permanent magnet or a temporary magnet?</b></summary>
<p>
<b>Ans:</b> It is a temporary magnet. Its magnetic field exists only as long as an electric current is flowing through the coil.
</p>
</details>

</div>