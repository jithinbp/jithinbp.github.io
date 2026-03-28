---
layout: manual
title: "AC Pickup from Mains"
date: 28 March 2026
image:
  path: /assets/img/seelab/school-level/images/ac-pickup.jpg
caption: Capturing the 50Hz electromagnetic field from domestic wiring
section: School Level Physics
---

## Experiment: Capturing AC Pickup from Domestic Wiring

### 1. Aim

To demonstrate the presence of electromagnetic fields around domestic electrical wiring and to observe the induced AC signal using a long wire as an antenna.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* A long flexible wire (approx. 1–2 meters)
* PC, Laptop, or Smartphone with SEELab3 software

### 3. Theory & Principle

All current-carrying conductors in our domestic wiring (carrying 230V, 50Hz AC) create a weak, oscillating electromagnetic field in their surroundings. This field is a form of "Electromagnetic Interference" (EMI).

When a long wire is connected to a high-impedance input like **A1**, it acts as a **Receiving Antenna**. The changing magnetic and electric fields from the room's wiring induce a tiny alternating voltage in this wire. 



The human body also acts as a large conductor. When you touch the tip of the wire, your body effectively increases the "antenna surface area," significantly increasing the magnitude of the induced 50Hz signal (or 60Hz depending on your region).

### 4. Circuit Diagram / Setup

1.  Connect one end of a long wire to the **A1** input.
2.  Leave the other end of the wire free (ensure it is not touching GND or any other terminal).
3.  Ensure the SEELab3 is connected to your computer or phone and the software is running.

### 5. Procedure

1.  Open the SEELab3 software and select the "Oscilloscope" tool.
2.  Enable the trace for **A1** and set the "Timebase" to **10 ms/div** or **20 ms/div**.
3.  Observe the waveform on the screen. Even with the wire hanging freely, you may see a small 50Hz sine wave.
4.  **Increase Pickup:** Touch the bare metal tip of the long wire with your finger. Observe the immediate increase in the amplitude of the sine wave.
5.  **Frequency Check:** Use the software's "Measure" or "Frequency" tool to verify that the captured signal is exactly **50 Hz** (or 60 Hz).
6.  **Power Source Test:** Observe the difference in amplitude when your laptop is running on battery versus when it is plugged into the wall charger.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/school-level/images/pickup-screen-pc.png" alt="Wire Pickup" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Fig A: Pickup from a long wire(Desktop App)</p>
    </div>
    
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/school-level/images/pickup-screen-phone.jpg" alt="Finger Pickup" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Fig B: Pickup increased by touching the tip</p>
    </div>

  </div>
</div>

### 6. Observation Table

| Setup | Observed Waveform | Frequency (Hz) | Peak Voltage (V) |
| :--- | :--- | :--- | :--- |
| Free Hanging Wire | | | |
| Touching Wire Tip | | | |
| Moving wire near power socket | | | |

### 7. Results and Discussion

* The presence of a 50Hz sine wave on the screen confirms that the wire is picking up electromagnetic radiation from the environment.
* Touching the wire increased the induced voltage to ________ V.
* The amount of induced voltage is typically higher when using a Desktop or Laptop because they are often connected to the mains earth, which provides a larger return path for the common-mode noise.

### 8. Precautions

1.  **Safety First:** Do **NOT** insert the wire into a wall power socket. This experiment only captures the *field* near the wiring.
2.  **Input Range:** The pickup signal is usually within a few volts. However, if the signal looks "flat" at the top and bottom, it has exceeded the input range of A1.
3.  **Isolation:** For a cleaner signal, move away from large electric motors or heavy machinery that might add noise to the 50Hz sine wave.

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **No 50Hz signal seen** | Wire is too short or frequency range is wrong. | Use a longer wire; adjust the "Timebase" to 10ms/div. |
| **Signal is very small** | You are in a heavily shielded room. | Move closer to a light switch or wall wiring. |
| **Waveform is not a sine wave** | Interference from switching power supplies (SMPS). | Turn off nearby LED lamps or chargers to see if the wave cleans up. |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why is the frequency of the captured signal exactly 50 Hz (or 60 Hz)?</b></summary>
<p>
<b>Ans:</b> This is the standard frequency of the AC mains power supply provided by the electricity department. The electromagnetic field oscillates at the same frequency as the current in the wires.
</p>
</details>

<details>
<summary><b>Q2. Why does touching the wire increase the amplitude of the signal?</b></summary>
<p>
<b>Ans:</b> The human body is a conductor. By touching the wire, you act as an extension of the antenna, increasing the surface area available to intercept the electric and magnetic fields in the room.
</p>
</details>

<details>
<summary><b>Q3. Is this signal an example of Electric field or Magnetic field coupling?</b></summary>
<p>
<b>Ans:</b> It is primarily <b>Capacitive (Electric field) coupling</b>. The domestic wire and your "antenna" wire act like two plates of a capacitor with air as the dielectric, allowing the AC potential to be "sensed" by the high-impedance input.
</p>
</details>

<details>
<summary><b>Q4. Why is the pickup less when the laptop is running on battery?</b></summary>
<p>
<b>Ans:</b> When on battery, the laptop is "floating" and not connected to the earth of the building. This reduces the potential difference between the environment and the SEELab's ground, resulting in a smaller measured signal.
</p>
</details>

<details>
<summary><b>Q5. Can this experiment be used to locate hidden wiring in a wall?</b></summary>
<p>
<b>Ans:</b> Yes. By moving the wire (antenna) across a wall, the amplitude of the 50Hz signal will peak when the wire is directly over a live power cable hidden behind the plaster.
</p>
</details>

</div>