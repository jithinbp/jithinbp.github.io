---
layout: manual
title: "AC Resistance of the Human Body"
date: 29 April 2026
image:
  path: /assets/img/seelab/school-level/images/ac-human-setup-seelab3.jpg
caption: AC human impedance using WG (input A1) and A2 (divider node)
section: Getting Started
---

## Measurement of AC Resistance / Impedance of the Human Body

### 1. Aim

To estimate the human body’s **AC impedance** using SEELab3 with an AC source (WG) and the built-in high input impedance at **A2**.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Connecting wires and two metal electrodes (coins/plates/strips)
* PC / Laptop / Android with SEELab3 software

### 3. Theory & Principle

This is a measurement using a **voltage divider** model:

* The human body behaves like an impedance $Z_{body}$.
* The SEELab3 input at **A2** has a known input impedance $R_{in}$, typically about $1\text{ M}\Omega$.

Let:
* $V_{A1}$ = RMS voltage at **A1** (across the whole divider)
* $V_{A2}$ = RMS voltage at **A2** (across $R_{in}$)

Current through the series path is:
$$
I=\frac{V_{A2}}{R_{in}}
$$

Voltage across the body is:
$$
V_{body}=V_{A1}-V_{A2}
$$

So the estimated impedance is:
$$
Z_{body}=\frac{V_{body}}{I}=(V_{A1}-V_{A2})\cdot\frac{R_{in}}{V_{A2}}
$$

For comparison/learning (at moderate frequency like `1000 Hz`), $Z_{body}$ can be reported in **kilo-ohms**.

### 4. Circuit Diagram / Setup

1. Connect the AC source **WG** (sine wave) to one electrode and also to **A1** for monitoring.
2. Connect the other electrode to **A2**.
3. Ensure SEELab3 `GND` reference is correctly wired (as per your hardware).
4. Keep electrode contact area similar between trials.

### 5. Procedure

1. Launch the SEELab3 app and open the **AC resistance / impedance** measurement screen (or oscilloscope/plot mode with $V_{rms}$ readouts).
2. Set:
   - **WG frequency** = `1000 Hz`
   - **WG amplitude** = start with a moderate value so RMS voltages stay within A1/A2 range.
3. Enable analysis/readout for:
   - **A1** (input RMS)
   - **A2** (output RMS)
4. Touch the electrodes with **intact skin** and hold contact stable for 3–5 seconds.
5. Record:
   - $V_{A1,\text{rms}}$
   - $V_{A2,\text{rms}}$
6. Calculate $Z_{body}$ using $R_{in}=1\text{ M}\Omega$:
$$
Z_{body}=(V_{A1}-V_{A2})\cdot\frac{10^6}{V_{A2}}
$$
7. Repeat for different contact conditions (dry, wet, increased contact area).

### 6. Observation Table

**Reference:** $R_{in} = 1.0\text{ M}\Omega$

| Condition | $V_{A1}$ RMS (V) | $V_{A2}$ RMS (V) | Estimated $Z_{body}$ (k$\Omega$) | Remarks |
| :--- | :--- | :--- | :---: | :--- |
| Dry hands | | | | |
| Dry hands with coin/contact increase | | | | |
| Wet hands | | | | |

### 7. Precautions

1. Use only the **low voltage AC output** from SEELab3 (WG). Never connect to AC mains.
2. Do **not** touch with cut/bruised skin or if you have any wound.
3. Keep contact stable to avoid large fluctuations.

### 8. Error Analysis

* At AC frequencies, the body impedance includes non-resistive components (skin capacitance), so $Z_{body}$ is an approximation.
* Contact pressure and contact area change $Z_{body}$ during measurement.
* Noise/trigger settings can affect RMS estimation.

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| RMS values look wrong or unstable | Weak/no contact between electrodes and skin | Reposition electrodes; maintain steady touch |
| $V_{A2}$ is very small | Divider is not formed correctly | Verify WG→electrode→body→A2 path |
| Computed $Z_{body}$ is unrealistically low/high | Wrong electrode polarity or wiring | Swap electrode connections and retake |

<div class="viva-section nosplit">

<h3> 10. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why do we need the high input impedance at A2?</b></summary>
<p>
<b>Ans:</b> Human body resistance is typically very high (often in the M$\Omega$ / hundreds of k$\Omega$ range). A high $R_{in}$ ensures the divider current is measurable and the voltage drop can be detected.
</p>
</details>

<details>
<summary><b>Q2. Derive the formula for $Z_{body}$ from $V_{A1}$ and $V_{A2}$.</b></summary>
<p>
<b>Ans:</b> Current is $I=V_{A2}/R_{in}$. Body voltage is $V_{body}=V_{A1}-V_{A2}$. So $Z_{body}=V_{body}/I=(V_{A1}-V_{A2})\cdot R_{in}/V_{A2}$.
</p>
</details>

<details>
<summary><b>Q3. Why does wetting hands decrease the measured resistance?</b></summary>
<p>
<b>Ans:</b> Water (with dissolved salts) improves ionic conduction through skin, reducing resistance/impedance and increasing divider current.
</p>
</details>

<details>
<summary><b>Q4. Is $Z_{body}$ purely resistive at AC?</b></summary>
<p>
<b>Ans:</b> No. Skin and electrode interfaces add non-ideal effects (capacitive/complex impedance), but divider-based measurement still gives a useful estimate for comparison.
</p>
</details>

</div>

