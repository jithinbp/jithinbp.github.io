---
layout: manual
title: "Clamping Circuit Using a PN Junction Diode"
date: 28 March 2026
image:
  path: /assets/img/seelab/electronics/images/clamping-setup.jpg
caption: Diode clamping circuit — the capacitor shifts the entire waveform, the diode sets the clamp level
section: Electronics
---

## Clamping Circuit Using a PN Junction Diode

### 1. Aim

To study the action of a **diode clamping circuit** — a circuit that shifts the entire AC waveform up or down by adding a DC offset — and to observe how the clamped output level is controlled by the DC bias applied through **PV1**.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* PN junction diode (1N4148)
* Capacitor $C = 1\text{ }\mu F$
* Connecting wires
* PC or Smartphone with SEELab3 software

---

### 3. Theory & Principle

#### 3.1 Clipper vs Clamper — the key distinction

A **clipper** (previous experiment) cuts away part of the waveform — the shape of the surviving portion is unchanged but some of it is removed. A **clamper** shifts the entire waveform up or down without altering its shape — the peak-to-peak amplitude is preserved, only the DC level changes.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/clamping-screen-phone.jpg" alt="Clamping — Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Mobile App</p>
    </div>
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/electronics/images/clamping-screen-pc.png" alt="Clamping — Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Desktop App</p>
    </div>
  </div>
</div>


#### 3.2 How the clamper works

The circuit consists of a series capacitor $C$ between WG and the output node, with a diode connecting the output node to PV1.

On the **first negative peak** of the input, the output node is pulled low and the diode becomes forward biased, clamping the output node to:

$$V_{clamp} = V_{PV1} - V_f \approx V_{PV1} - 0.6\text{ V}$$

The capacitor charges rapidly to the difference $V_{in,\text{neg\_peak}} - V_{clamp}$ and holds this charge. On subsequent cycles the capacitor's stored voltage acts as a DC offset, shifting the entire waveform upward so that the negative peaks sit at $V_{clamp}$.

For a $3\text{ V}$ peak sinusoid and $V_{PV1} = 1\text{ V}$:

$$V_{clamp} = 1.0 - 0.6 = 0.4\text{ V} \approx 0.3\text{ V (measured)}$$

The entire waveform is lifted so its lowest point sits at $\approx +0.3\text{ V}$, and the positive peak rises to $\approx 0.3 + 6 = 6.3\text{ V}$ (peak-to-peak preserved at $6\text{ V}$).

> **Important:** The output peak-to-peak voltage equals the input peak-to-peak — the clamper adds DC offset only. This is what distinguishes it from a clipper, which reduces peak-to-peak.

#### 3.3 Reverse clamping

Reversing the diode flips the action — the diode now clamps the **positive** peaks instead of the negative ones, shifting the entire waveform downward. Applying a negative voltage to PV1 with the reversed diode clamps the positive peaks below zero.

---

### 4. Circuit Diagram / Setup

1. Connect **WG** to one plate of capacitor $C$ ($1\text{ }\mu F$). Connect **A1** to WG to monitor the input.
2. Connect the other plate of $C$ to the **anode** of the diode. This is the output node — connect it to **A2**.
3. Connect the **cathode** of the diode to **PV1**.

> For reverse clamping: swap the diode (cathode to output node, anode to PV1) and apply negative voltages on PV1.

---

### 5. Procedure

#### Part A — Positive (upward) clamping

1. Open the SEELab3 app. Set WG to a sinusoidal output at **$f = 1000\text{ Hz}$**, amplitude $\approx 3\text{ V}$ peak.
2. Set **PV1 = 1 V**. Click **"Start"** and observe A1 and A2.
   * A1 shows the original symmetric sinusoid centred on $0\text{ V}$.
   * A2 should show the same waveform shifted upward — negative peaks lifted to $\approx V_{PV1} - 0.6\text{ V}$.
3. Confirm the **peak-to-peak amplitude** of A2 equals that of A1.
4. Vary PV1: **0 V, 0.5 V, 1.0 V, 1.5 V, 2.0 V**. Record the clamped negative-peak level each time.

#### Part B — Reverse (downward) clamping

5. **Reverse the diode** and set PV1 to negative values: **0 V, −0.5 V, −1.0 V, −1.5 V**.
6. Observe that the positive peaks are now clamped and the waveform shifts downward.
7. Record the clamped positive-peak level at each PV1 setting.

---

### 6. Observation Table

**Frequency:** ________ Hz &emsp;|&emsp; **$V_{in,\text{peak}}$:** ________ V &emsp;|&emsp; **$V_{in,\text{p-p}}$:** ________ V

#### 6a. Part A — Positive Clamping

| PV1 (V) | Theoretical $V_{neg\_peak} = V_{PV1} - 0.6$ (V) | Measured $V_{neg\_peak}$ (V) | Measured $V_{p\text{-}p}$ at A2 (V) |
| :---: | :---: | :---: | :---: |
| 0.0 | −0.6 | | |
| 0.5 |  0.9 | | |
| 1.0 |  0.4 | | |
| 1.5 |  0.9 | | |
| 2.0 |  1.4 | | |

#### 6b. Part B — Reverse Clamping (diode reversed)

| PV1 (V) | Theoretical $V_{pos\_peak} = V_{PV1} + 0.6$ (V) | Measured $V_{pos\_peak}$ (V) | Measured $V_{p\text{-}p}$ at A2 (V) |
| :---: | :---: | :---: | :---: |
|  0.0 |  0.6 | | |
| −0.5 |  0.1 | | |
| −1.0 | −0.4 | | |
| −1.5 | −0.9 | | |

---

### 7. Results and Discussion

* With PV1 = 1 V, the negative peaks of the output were clamped to ________ V, against a theoretical value of $1.0 - 0.6 = 0.4\text{ V}$.
* The peak-to-peak amplitude at A2 was ________ V, equal to the input peak-to-peak of ________ V, confirming that the clamper preserves waveform shape and only shifts the DC level.
* As PV1 was increased, the clamped level rose proportionally — each $1\text{ V}$ increase in PV1 raised the output by $1\text{ V}$, verifying $V_{clamp} = V_{PV1} - V_f$.
* With the diode reversed and PV1 negative, the waveform shifted downward symmetrically, confirming that the clamping direction is controlled entirely by diode orientation and PV1 polarity.

---

### 8. Precautions

1. **Capacitor value:** The capacitor must fully charge within the first few cycles for steady-state clamping to be established. For $f = 1000\text{ Hz}$, $C = 1\text{ }\mu F$ with the $1\text{ M}\Omega$ input impedance of A2 gives $\tau = RC = 1\text{ s}$ — very long. In practice the diode provides a fast charge path on the clamping half-cycle; however, the discharge through $1\text{ M}\Omega$ is slow, which is what holds the DC shift. Do not add a low-value load resistor across the output — it will discharge the capacitor too quickly and degrade the clamping action.
2. **A2 input impedance dependence:** The clamped DC level depends on the $1\text{ M}\Omega$ input impedance of A2 holding the capacitor charge between cycles. With a real load (e.g., $10\text{ k}\Omega$) the clamping will degrade — the practical clamper needs a buffer amplifier for low-impedance loads.
3. **Allow settling:** The output takes a few cycles to settle to steady-state after changing PV1. Wait briefly before recording measurements.
4. **Capacitor polarity:** If an electrolytic capacitor is used, it must be oriented correctly. Preferred: use a non-polarised film or ceramic capacitor for this experiment.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **A2 shows same waveform as A1 — no DC shift** | Capacitor missing, shorted, or not making contact. | Verify capacitor is in series between WG and the output node; test with multimeter. |
| **DC shift present but waveform is distorted** | Diode is in wrong orientation — clipping instead of clamping. | Check diode direction; in Part A the anode goes to the output node, cathode to PV1. |
| **Clamped level drifts slowly** | Capacitor discharging through A2's $1\text{ M}\Omega$ impedance between cycles at low frequency. | Increase frequency to 1000 Hz or above so the period is much shorter than $\tau = RC$. |
| **Peak-to-peak at A2 is smaller than at A1** | Clipper behaviour — a resistor may be accidentally in series, or wrong circuit built. | Confirm no series resistor is present; a pure clamper has only $C$ and the diode. |

---

<div class="viva-section nosplit">

<h3>10. Viva-Voce Questions</h3>

<details>
<summary><b>Q1. What role does the capacitor play in the clamping circuit?</b></summary>
<p>
<b>Ans:</b> The capacitor serves as a DC-blocking and charge-storage element. On the first clamping half-cycle, the diode conducts and the capacitor charges to the difference between the input peak and the clamping voltage. This stored charge acts as a battery — it adds a fixed DC voltage in series with the AC signal on every subsequent cycle, effectively shifting the entire waveform. The capacitor must retain its charge between cycles (i.e., the discharge time constant $\tau = R_{load}C$ must be much larger than the signal period) for steady clamping to be maintained.
</p>
</details>

<details>
<summary><b>Q2. Why is the clamped level $V_{PV1} - V_f$ rather than $V_{PV1}$?</b></summary>
<p>
<b>Ans:</b> The diode conducts when its anode (output node) is more positive than its cathode (PV1) by $V_f \approx 0.6\text{ V}$. It stops conducting — and therefore clamps — when the output node reaches exactly $V_{PV1} - V_f$ during the negative peak, not $V_{PV1}$. The $V_f$ drop across the forward-biased diode subtracts from the bias, so the final clamped level is always one diode drop below (for this orientation) the applied bias voltage.
</p>
</details>

<details>
<summary><b>Q3. The positive peak of the clamped output is much higher than the original input peak. Is this a problem?</b></summary>
<p>
<b>Ans:</b> Not a circuit problem — it is the expected behaviour. If the negative peak is lifted by $\Delta V$ (the DC shift), the positive peak is also lifted by the same $\Delta V$, since the entire waveform shifts rigidly. Practically, this means the downstream circuit (and the A2 input channel) must be able to handle this elevated positive swing without clipping or damage.
</p>
</details>

<details>
<summary><b>Q4. Where is clamping used in real electronic systems?</b></summary>
<p>
<b>Ans:</b> Clampers appear in several practical applications: (1) <b>Television sync restoration</b> — the sync tip of a composite video signal is clamped to a reference level at the start of each line to remove noise-induced DC wander. (2) <b>Voltage multiplier circuits</b> — cascaded clampers and peak detectors (Cockcroft-Walton ladder) progressively stack DC offsets to multiply a low AC voltage to a high DC voltage without a transformer. (3) <b>Coupling with level shifting</b> — when an AC signal from one stage needs to be shifted to a specific DC operating point before entering the next stage.
</p>
</details>

</div>