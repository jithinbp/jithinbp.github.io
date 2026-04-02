---
layout: manual
title: "Ultrasonic Distance Measurement"
date: 28 March 2026
image:
  path: /assets/img/seelab/school-level/images/sr04-setup-seelab3.jpg
caption: Measuring distance and studying free fall using ultrasound
section: School Level Physics
---

## Distance Measurement and Free Fall using Ultrasound

### 1. Aim

To measure the distance of an object using an HC-SR04 ultrasonic sensor and to study the motion of a freely falling body to determine the acceleration due to gravity ($g$).

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* HC-SR04 Ultrasonic Sensor module
* A flat reflecting surface (for distance) and a flat plate (for free fall)
* Jumper wires (Female-to-Male)
* PC or Smartphone with SEELab3 software

### 3. Theory & Principle

The HC-SR04 sensor uses **Time of Flight (ToF)** of sound waves to measure distance. It contains two piezoelectric discs: one transmits a $40\text{ kHz}$ ultrasonic pulse, and the other receives the reflected echo.



The distance ($S$) is calculated as:
$$S = \frac{v \times t}{2}$$
Where $v$ is the speed of sound ($\approx 340\text{ m/s}$) and $t$ is the time interval between trigger and echo.

<img src="/assets/img/seelab/school-level/images/sr04-screen-phone.jpg" style="width: 60%; display: block; margin: 0 auto;">


**Free Fall:**
For a body falling from rest, the distance traveled follows the equation:
$$S = \frac{1}{2}gt^2$$
By plotting $S$ against $t$, we can observe a parabolic trajectory and calculate $g$ from the curve fit.



### 4. Circuit Diagram / Setup

1.  **Vcc:** Connect to the **5V** terminal of SEELab3.
2.  **Trig:** Connect to the **SQ2** output.
3.  **Echo:** Connect to the **IN2** input.
4.  **GND:** Connect to any **GND** terminal.
5.  **For Free Fall:** Mount the sensor facing downwards on a stand at a height of $\approx 1.5\text{m}$.

### 5. Procedure

#### **Part A: Distance Measurement**
1.  Open the SEELab3 software and select the "Ultrasonic Distance" tool.
2.  Hold a flat object in front of the sensor.
3.  Observe the live distance reading and the real-time plot.
4.  Verify the accuracy using a standard ruler.

#### **Part B: Measurement on a Freely Falling Body**
1.  Execute the Python program for distance measurement.
2.  Hold a flat plate just below the sensor facing downwards.
3.  release the plate.
4.  The Python script will plot the distance as a function of time.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/school-level/images/sr04-falling-body-setup.jpg" alt="Distance Plot" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Fig A: Falling body setup</p>
    </div>
    
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/school-level/images/sr04-freefall-plot.png" alt="Falling Data" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Fig B: Free fall parabolic data</p>
    </div>

  </div>
</div>

### 6. Observation Table

| Actual Distance (cm) | Measured Distance (cm) | Calculated $g$ (from plot) |
| :--- | :--- | :--- |
| 10.0 | | |
| 30.0 | | |
| 50.0 | | |
| **Mean Value** | | **$g \approx$ ________ $\text{m/s}^2$** |

### 7. Results and Discussion

* The distance measurement confirmed the "Time of Flight" principle using ultrasound.
* The free-fall data followed a parabolic path, verifying the equation $S = \frac{1}{2}gt^2$.
* The value of $g$ was calculated as ________ $\text{m/s}^2$. Discrepancies may arise from air resistance on the falling plate.

### 8. Python Programming & Data

* [Download Python Program for Distance Measurement](https://expeyes.in/software/python/sr04_dist.py)
* [Download Python Program for Falling Body Analysis](https://expeyes.in/software/python/sr04_gravity.py)
* [Download Sample Data](https://expeyes.in/data/sr04_sample.dat)

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **Reading stays at 0** | Echo/Trig swapped. | Verify Trig is on SQ2 and Echo is on IN2. |
| **Noisy Falling Data** | Plate wobbled. | Use a stiffer flat plate and release it carefully. |
| **Inaccurate Distance** | Speed of sound error. | Check room temperature; sound speed varies with temperature. |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why is the time divided by 2 in the distance formula?</b></summary>
<p>
<b>Ans:</b> The time measured is the round-trip time (to the object and back). Dividing by 2 gives the time for a one-way trip.
</p>
</details>

<details>
<summary><b>Q2. What is the frequency used by the SR04 sensor?</b></summary>
<p>
<b>Ans:</b> It uses $40\text{ kHz}$ ultrasound, which is above the human audible range.
</p>
</details>

<details>
<summary><b>Q3. Why does the falling body graph look like a parabola?</b></summary>
<p>
<b>Ans:</b> Because the displacement $S$ is proportional to the square of time $t$ under constant acceleration ($g$).
</p>
</details>

<details>
<summary><b>Q4. Can this sensor measure distance in a vacuum?</b></summary>
<p>
<b>Ans:</b> No. Sound waves require a medium (like air) to travel.
</p>
</details>

<details>
<summary><b>Q5. How does temperature affect the speed of sound?</b></summary>
<p>
<b>Ans:</b> Speed of sound increases with temperature ($\approx 0.6\text{ m/s}$ per degree Celsius).
</p>
</details>

</div>