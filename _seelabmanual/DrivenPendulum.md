---
layout: manual
title: "Driven Pendulum and Resonance"
date: 27 March 2026
image:
  path: /assets/img/seelab/school-level/images/driven-pend-setup-eyes17.jpg
caption: Observing resonance in a magnetically driven pendulum
section: School Level Physics
---

## Experiment: Driven Pendulum and Resonance

### 1. Aim

To study the behavior of a driven pendulum, determine its natural frequency, and demonstrate the phenomenon of resonance using a periodic magnetic force.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Solenoid coil (approx. 3000 turns)
* Two small button-shaped magnets
* A strip of paper and adhesive tape (to construct the pendulum)
* Rigid support/stand
* Connecting wires

### 3. Theory & Principle

A simple pendulum undergoes periodic motion, transferring energy between kinetic and potential modes. Its **natural frequency** ($f_0$) is determined by its length ($L$) from the pivot to the center of mass, and the acceleration due to gravity ($g$):

$$T = 2\pi\sqrt{\frac{L}{g}} \quad \implies \quad f_0 = \frac{1}{2\pi}\sqrt{\frac{g}{L}}$$



In a **driven oscillation**, an external periodic force is applied to the system. If the frequency of this external force ($f_{drive}$) matches the natural frequency of the pendulum ($f_0$), the system absorbs energy most efficiently, and the amplitude of oscillation increases significantly. This condition is known as **Resonance**.



### 4. Setup & Circuit (Common for both Apps)

1.  **Pendulum Construction:** Tape two button magnets to the bottom of a 5–10 cm paper strip. Suspend the strip from a rigid support so it can swing freely.
2.  **Driving Mechanism:** Place the solenoid coil directly below the equilibrium position of the magnets. Align it so the magnetic field acts vertically on the magnets.
3.  **Connections:** Connect the solenoid coil between the signal output (**SQ1** or **PV1**) and **GND**.

---

## Mobile App Setup (Using SQ1)

### 5. Procedure (Mobile App with SQ1)

In this setup, the solenoid coil acts as an electromagnet. When connected to the **SQ1** (Square Wave) output, it creates a periodic magnetic pulse that exerts a force on the magnets.

1.  Measure the length ($L$) of your pendulum in meters.
2.  Calculate the theoretical natural frequency: $f_0 = \frac{1}{2\pi}\sqrt{\frac{9.8}{L}}$.
3.  Open the SEELab3 mobile app and select the "Driven Pendulum" tool.
4.  Set **SQ1** to a frequency well below your calculated $f_0$.
5.  Slowly increase the frequency in small steps (e.g., $0.1\text{ Hz}$) and observe the amplitude of the pendulum's swing.
6.  Identify the frequency at which the amplitude is maximum. This is the **Resonant Frequency**.

<img src="/assets/img/seelab/school-level/images/driven-pend-screen-phone.jpg" style="width: 55%; display: block; margin: 0 auto;">

---

## Desktop App Setup (Using PV1)

### 6. Procedure (Desktop App with PV1)

In the desktop version, the software can oscillate the **PV1** (+/-5V DC) output back and forth in a smooth sine wave motion to drive the pendulum more gently.

1.  Open the SEELab3 desktop software and select the **"Driven Pendulum Resonance"** experiment under the Mechanics section.
2.  Follow the same steps as the mobile procedure, using the frequency slider for PV1.
3.  Observe the "Phase" of the oscillation—notice how the pendulum's timing relative to the drive changes as you pass through resonance.

<img src="/assets/img/seelab/school-level/images/driven-pend-desktop.png" style="width: 100%; display: block; margin: 0 auto;">

---

### 7. Observation Table

**Pendulum Length ($L$):** ________ cm  
**Theoretical Frequency ($f_0$):** ________ Hz

| Driving Frequency (Hz) | Observed Amplitude (Small/Medium/Large) |
| :--- | :--- |
| $f_0 - 1.0$ | |
| $f_0 - 0.5$ | |
| **$f_{resonant}$** | |
| $f_0 + 0.5$ | |
| $f_0 + 1.0$ | |

### 8. Error Analysis

* **Damping Effects:** Air resistance and friction at the pivot point "damp" the oscillation, which slightly lowers the resonant frequency and limits the maximum amplitude.
* **Effective Length:** The formula assumes all mass is at a single point. If the paper strip is heavy relative to the magnets, the "center of oscillation" shifts, affecting $f_0$.
* **Coil Position:** If the coil is not perfectly centered, the driving force will have a horizontal component, causing the pendulum to wobble or "precess" rather than swing in a straight line.

### 9. Results and Discussion

* The natural frequency was found to be ________ Hz experimentally.
* Resonance occurred when the frequency of the drive was **equal to** the natural frequency.
* At resonance, the transfer of energy from the magnetic field to the pendulum was **maximum**.

### 10. Precautions

1.  **Alignment:** Ensure the coil is close enough to influence the magnets but not so close that the pendulum hits the coil.
2.  **Damping:** Perform the experiment in a draft-free area to minimize air resistance.
3.  **Current:** Avoid running high currents through the coil for long durations to prevent overheating.

### 11. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **No movement at all** | Coil not connected. | Check wiring and ensure SQ1/PV1 is active. |
| **Weak oscillations** | Magnets are too far. | Move the coil closer to the equilibrium point. |
| **Resonance not found** | Steps too large. | Change the frequency in smaller increments ($0.05\text{ Hz}$). |

<div class="viva-section nosplit">

<h3> 12. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. What is the difference between free, forced, and resonant oscillations?</b></summary>
<p>
<b>Ans:</b> <b>Free oscillation</b> occurs when a system is displaced and released (vibrates at $f_0$). <b>Forced oscillation</b> is when an external periodic force is applied at any frequency. <b>Resonant oscillation</b> is a specific case of forced oscillation where the drive frequency matches $f_0$, causing maximum amplitude.
</p>
</details>

<details>
<summary><b>Q2. How does the length of the pendulum affect the resonant frequency?</b></summary>
<p>
<b>Ans:</b> Frequency is inversely proportional to the square root of length ($f \propto 1/\sqrt{L}$). Therefore, increasing the length of the pendulum will decrease its resonant frequency.
</p>
</details>

<details>
<summary><b>Q3. Why does the amplitude eventually stop increasing at resonance?</b></summary>
<p>
<b>Ans:</b> In a real system, energy is lost due to friction and air resistance (damping). At resonance, the amplitude grows until the energy lost to damping per cycle exactly equals the energy provided by the driving force.
</p>
</details>

<details>
<summary><b>Q4. What is the phase relationship at resonance?</b></summary>
<p>
<b>Ans:</b> At resonance, the displacement of the pendulum lags behind the driving force by exactly $90^\circ$ ($\pi/2$ radians).
</p>
</details>

<details>
<summary><b>Q5. Can resonance be dangerous in real-world structures?</b></summary>
<p>
<b>Ans:</b> Yes. If wind or earthquakes create periodic forces that match the natural frequency of bridges or buildings, the resulting high-amplitude oscillations can lead to structural failure (e.g., the Tacoma Narrows Bridge).
</p>
</details>

</div>