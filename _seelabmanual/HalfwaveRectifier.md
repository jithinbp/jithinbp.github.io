---
layout: manual
title: "Half-Wave Rectifier Using a PN Junction Diode"
date: 28 March 2026
image:
  path: /assets/img/seelab/electronics/images/halfwave-setup-seelab3.jpg
caption: Half-wave rectifier circuit with optional filter capacitor
section: Electronics
---

## Experiment: Half-Wave Rectifier Using a PN Junction Diode

### 1. Aim

To study the rectifying action of a PN junction diode by constructing a **half-wave rectifier**, to observe the difference between the ideal textbook waveform and the actual output, to investigate the effect of **junction capacitance** on the reverse-half output, and to study the **smoothing effect** of a filter capacitor on the rectified waveform.

---

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* PN junction diode — **1N4148** (low junction capacitance, $C_j \approx 4\text{ pF}$)
* PN junction diode — **1N4007** (higher junction capacitance, $C_j \approx 20\text{ pF}$) for comparison
* Load resistor $R_L = 1\text{ k}\Omega$
* Filter capacitor $C = 1\text{ }\mu F$
* Breadboard and connecting wires
* PC or Smartphone with SEELab3 / ExpEYES software

---

### 3. Theory & Principle


#### 3.1 The PN Junction as a Rectifier

A PN junction diode conducts current freely when **forward biased** (anode positive with respect to cathode) and blocks current when **reverse biased**. When an AC sinusoidal voltage is applied to a series circuit of a diode and a load resistor $R_L$:

* **Positive half-cycle:** The diode is forward biased and conducts. Current flows through $R_L$ and a positive output voltage appears.
* **Negative half-cycle:** The diode is reverse biased and ideally blocks all current. The output voltage across $R_L$ is zero.

Since only one half of the AC cycle appears at the output, this is called **half-wave rectification**.

#### 3.2 Deviation from the Ideal Textbook Waveform

Many textbooks depict the output as a perfect half-sinusoid that begins exactly at $0\text{ V}$ and reaches the same peak as the input. The actual output differs in two important ways:

**Forward voltage drop ($V_f$):** A real silicon diode requires a minimum forward voltage of approximately $0.6$–$0.7\text{ V}$ before it begins to conduct significantly. The output therefore:

* Starts conducting only when $V_{in} > V_f \approx 0.6\text{ V}$ (the **threshold** or **cut-in voltage**)
* Has a peak amplitude reduced by $V_f$ compared to the input peak:

$$V_{out,\text{peak}} = V_{in,\text{peak}} - V_f$$

For $V_{in,\text{peak}} = 3\text{ V}$ and $V_f \approx 0.6\text{ V}$, the output peak is approximately $2.4\text{ V}$.

#### 3.3 Junction Capacitance and Reverse-Half Leakage

Every PN junction has a small **junction capacitance** $C_j$ in parallel with the ideal diode. Its value depends on the diode type:

| Diode | $C_j$ (typical) | Application |
| :--- | :---: | :--- |
| 1N4148 | $\approx 4\text{ pF}$ | Signal / high-speed switching |
| 1N4007 | $\approx 20\text{ pF}$ | Mains rectification (50/60 Hz) |

During the **reverse half-cycle**, this capacitance couples a small fraction of the input signal to the output through capacitive displacement current. The effect is:

* **Visible at high frequencies** (e.g., 1000 Hz) because $Z_C = 1/(2\pi f C_j)$ becomes small enough to pass a measurable signal.
* **Not visible at low frequencies** (e.g., 50 Hz) because $Z_C$ is very large.
* **Suppressed by a load resistor:** When $R_L = 1\text{ k}\Omega$ is connected, the tiny charge coupled through $C_j$ is quickly discharged through $R_L$, producing negligible voltage. Without $R_L$, the $1\text{ M}\Omega$ input impedance of A2 allows the capacitively-coupled charge to build up to a visible level.

#### 3.4 The RC Filter (Smoothing)

The pulsating DC output of a half-wave rectifier contains a large **ripple** — the output alternates between the rectified peaks and zero. A capacitor $C$ connected in parallel with $R_L$ reduces this ripple:

* On the **conducting half-cycle**, $C$ charges rapidly to the peak output voltage.
* On the **non-conducting half-cycle**, $C$ discharges slowly through $R_L$, maintaining the output voltage at a nearly constant level instead of falling to zero.

The **ripple voltage** (peak-to-peak) is approximately:

$$V_{ripple} \approx \frac{V_{out,\text{peak}}}{f \cdot R_L \cdot C}$$

where $f$ is the AC frequency. A larger $RC$ product means slower discharge and lower ripple. For $f = 1000\text{ Hz}$, $R_L = 1\text{ k}\Omega$, $C = 1\text{ }\mu F$: $RC = 1\text{ ms} = 1$ time period — moderate ripple. Increasing $C$ to $10\text{ }\mu F$ gives $RC = 10\text{ ms}$, reducing ripple significantly.

---


<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/halfwave-screen-phone.jpg" alt="Distance Plot" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Halfwave (No Filter Capacitor. Notice voltage drop)</p>
    </div>    
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/halfwave-with-filter-screen.png" alt="Falling Data" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Half Wave With Filter</p>
    </div>
  </div>
</div>

### 4. Circuit Diagram / Setup

**Part A — Basic half-wave rectifier (no filter capacitor):**

1. Connect the **anode** of the diode to **WG**.
2. Connect the **cathode** of the diode to one end of $R_L$.
3. Connect the other end of $R_L$ to **GND**.
4. Connect **WG** to **A1** (monitors $V_{in}$).
5. Connect the junction of the diode cathode and $R_L$ to **A2** (monitors $V_{out}$).

**Part B — With RC filter:**

6. Connect the filter capacitor $C = 1\text{ }\mu F$ in **parallel with $R_L$** (between A2 node and GND). Do not add this capacitor until Part A observations are complete.

> **Note on junction capacitance test:** To observe the $C_j$ effect clearly, temporarily **remove $R_L$** (open-circuit load) and use a **1N4007** diode at 1000 Hz. The $1\text{ M}\Omega$ input impedance of A2 will allow the reverse-half leakage to become visible.

---

### 5. Procedure

#### Part A — Basic Rectifier

1. Open the SEELab3 / ExpEYES app and select the **"Half-Wave Rectifier"** experiment.
2. Set the WG to a **sinusoidal output** at **$f = 1000\text{ Hz}$**, amplitude $\approx 3\text{ V}$ peak.
3. Click **"Start"**. Observe both traces:
   * **A1** — the input sinusoidal voltage
   * **A2** — the rectified output across $R_L$
4. Note the following from the display:
   * The peak amplitude of A2 compared to A1 — the difference is the diode forward voltage drop $V_f$.
   * The input voltage at which the output just begins to appear — this is the cut-in voltage $V_{th}$.
   * The shape of the output during the negative half-cycle — it should be near zero (with $R_L$ connected).
5. **Sketch** both waveforms and compare with the ideal textbook picture.

#### Part B — Junction Capacitance Effect

6. **Remove $R_L$** from the circuit (open-circuit output). Keep A2 connected directly at the diode cathode.
7. Replace the 1N4148 with a **1N4007** diode.
8. Observe the A2 trace during the negative half-cycle — a small sinusoidal signal should now be visible, caused by capacitive coupling through $C_j$.
9. Restore $R_L = 1\text{ k}\Omega$ and observe that the reverse-half signal disappears.

#### Part C — RC Filter

10. Reconnect the 1N4148 and $R_L = 1\text{ k}\Omega$.
11. Connect the filter capacitor $C = 1\text{ }\mu F$ in parallel with $R_L$.
12. Observe the A2 trace — the output should now be a near-DC level with a small ripple superimposed.
13. Note the **ripple amplitude** and the **average DC level**.




---

### 6. Observation Table

**Diode used:** ________ &emsp;|&emsp; **$R_L$:** ________ $\Omega$ &emsp;|&emsp; **Frequency:** ________ Hz

#### 6a. Part A — Basic Rectifier

| Quantity | Measured Value |
| :--- | :---: |
| Input peak voltage $V_{in,\text{peak}}$ (V) | |
| Output peak voltage $V_{out,\text{peak}}$ (V) | |
| Forward voltage drop $V_f = V_{in,\text{peak}} - V_{out,\text{peak}}$ (V) | |
| Cut-in threshold voltage $V_{th}$ (V) | |
| Output voltage during negative half-cycle (V) | |
| Phase of output relative to input | In phase / Inverted |

#### 6b. Part B — Junction Capacitance (no $R_L$, 1N4007 at 1000 Hz)

| Condition | Reverse-half peak voltage at A2 (V) |
| :--- | :---: |
| 1N4007, no $R_L$ (open circuit) | |
| 1N4007, $R_L = 1\text{ k}\Omega$ | |
| 1N4148, no $R_L$ (open circuit) | |

#### 6c. Part C — RC Filter

| Filter capacitor $C$ | Ripple voltage $V_{ripple}$ (V) | Average output $V_{avg}$ (V) |
| :---: | :---: | :---: |
| None (no capacitor) | | |
| $1\text{ }\mu F$ | | |

---

### 7. Results and Discussion

* The diode conducted only during the positive half-cycle, producing a half-wave rectified output, as expected.
* The output peak was ________ V, which is ________ V less than the input peak of ________ V, consistent with the silicon diode forward voltage drop of $\approx 0.6\text{ V}$.
* The output began appearing only when $V_{in}$ exceeded the cut-in voltage of ________ V, confirming the **threshold behavior** absent in the ideal textbook model.
* With the 1N4007 and no load resistor, a reverse-half signal of ________ V peak was observed, attributed to capacitive coupling through the $20\text{ pF}$ junction capacitance. Connecting $R_L$ reduced this to ________ V, demonstrating that the effect is suppressed by a low-impedance load.
* Adding a $1\text{ }\mu F$ filter capacitor reduced the ripple from ________ V (no filter) to ________ V, raising the average DC output to ________ V.

---

### 8. Precautions

1. **Diode polarity:** Verify the cathode (marked with a band) is connected toward the load ($R_L$) and the anode toward WG. Reversing the diode will block the positive half and pass the negative half instead.
2. **WG amplitude:** Keep the peak input voltage within $\pm 3.3\text{ V}$ to stay within the safe input range of A1 and A2.
3. **Capacitor sequence:** Observe the basic rectifier waveform thoroughly **before** connecting the filter capacitor — adding it too early masks the individual half-cycle shape.
4. **Capacitor polarity:** If using an electrolytic capacitor for $C$, connect the positive terminal to the A2 (output) node and negative to GND. Reversing it can damage the capacitor.
5. **Frequency for junction capacitance test:** The $C_j$ coupling effect is only visible at **high frequencies** (≥ 500 Hz). At 50 Hz the reactance of even 20 pF is $\approx 160\text{ M}\Omega$ — far too high to produce a measurable signal.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **A2 shows no output at all** | Diode inserted backwards. | Swap the diode orientation; re-check cathode band direction. |
| **A2 shows the full sine wave (both halves)** | Diode is short-circuited or bypassed; wrong node monitored. | Check breadboard for solder bridges or misplaced wires; confirm A2 is at the cathode–$R_L$ junction. |
| **Output peak equals input peak (no $V_f$ drop)** | A1 and A2 both connected to same node (before the diode). | Verify A2 is after the diode, not at the WG terminal. |
| **Ripple does not reduce after adding capacitor** | Capacitor not in parallel with $R_L$, or capacitor is faulty/open. | Confirm capacitor is connected between A2 node and GND; test capacitor with a multimeter. |
| **Negative half shows large signal even with $R_L$ connected** | $R_L$ not making proper contact in breadboard. | Re-seat $R_L$; verify with multimeter in resistance mode. |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. What is rectification, and why is a diode suitable for this purpose?</b></summary>
<p>
<b>Ans:</b> Rectification is the conversion of an alternating current (AC) — which periodically reverses direction — into a unidirectional (DC) current. A PN junction diode is suitable because it has strongly asymmetric conductance: it offers very low resistance when forward biased (conducts) and very high resistance when reverse biased (blocks). This one-way valve action allows only one half of the AC cycle to reach the load.
</p>
</details>

<details>
<summary><b>Q2. Why does the actual output peak differ from the input peak, and why does conduction not begin at $0\text{ V}$?</b></summary>
<p>
<b>Ans:</b> A real silicon diode has a built-in potential barrier of approximately $0.6$–$0.7\text{ V}$ at the junction. The forward-biasing voltage must first overcome this barrier before significant current flows. Consequently: (1) the output does not appear until $V_{in}$ exceeds the cut-in voltage $V_{th} \approx 0.6\text{ V}$, and (2) the conducting portion of the waveform is shifted down by $V_f$, so the output peak $= V_{in,\text{peak}} - V_f$. Ideal diode models in textbooks ignore $V_f$, which is why they show a perfect half-sinusoid starting at $0\text{ V}$.
</p>
</details>

<details>
<summary><b>Q3. What is junction capacitance, and under what conditions does it cause a problem in a rectifier?</b></summary>
<p>
<b>Ans:</b> Junction capacitance $C_j$ is a parasitic capacitance that exists across every reverse-biased PN junction, arising from the depletion region acting as a dielectric between two charge layers. During the reverse half-cycle, $C_j$ passes a displacement current $I = C_j \cdot dV/dt$, coupling a small fraction of the input to the output. This becomes significant when: (a) the frequency is high (large $dV/dt$), (b) the diode has a large $C_j$ (e.g., 1N4007 at 20 pF), and (c) the load impedance is high (no $R_L$ to discharge the coupled charge). At mains frequency (50 Hz) with a 1 k$\Omega$ load, the effect is completely negligible.
</p>
</details>

<details>
<summary><b>Q4. Explain how a filter capacitor reduces the ripple in the rectified output.</b></summary>
<p>
<b>Ans:</b> When the diode conducts (positive half-cycle), the capacitor charges rapidly to the peak output voltage $V_{peak}$. When the diode stops conducting (negative half-cycle), instead of the output falling to zero, the capacitor discharges slowly through $R_L$ with a time constant $\tau = R_L C$. If $\tau \gg T$ (the period of the AC signal), the voltage hardly falls before the next positive peak recharges the capacitor — the output becomes a nearly smooth DC level with a small exponential ripple superimposed. The larger the $RC$ product, the smaller the ripple.
</p>
</details>

<details>
<summary><b>Q5. What are the disadvantages of a half-wave rectifier compared to a full-wave rectifier?</b></summary>
<p>
<b>Ans:</b> Three main disadvantages: (1) <b>Low average output voltage</b> — the average DC value of a half-wave rectified sine is $V_{avg} = V_{peak}/\pi \approx 0.318\,V_{peak}$, compared to $2V_{peak}/\pi \approx 0.636\,V_{peak}$ for full-wave. (2) <b>High ripple</b> — the ripple frequency equals the input frequency $f$, requiring a larger filter capacitor for the same smoothing compared to full-wave rectification where the ripple frequency is $2f$. (3) <b>Poor transformer utilization</b> — the transformer core carries DC-biased current, increasing hysteresis losses and reducing efficiency.
</p>
</details>

</div>