---
layout: manual
title: "Lemon Cell: Measuring EMF of Metal Pairs"
date: 27 March 2026
image:
  path: /assets/img/seelab/GetStart/images/lemoncell-setup-eyes17.jpg
caption: Measuring lemon-cell voltage for different electrode pairs
section: Getting Started
---

## Lemon Cell Experiment

### 1. Aim

To construct a lemon cell and measure the EMF produced by different metal electrode pairs using one SEELab input channel.

### 2. Apparatus / Components Required

* SEELab3 or ExpEYES-17 unit
* Connecting wires / crocodile clips
* 1-2 lemons (or any acidic fruit)
* Common metal electrodes (for example: Zinc nail, Copper strip/coin, Iron nail, Aluminium strip)
* A PC, Laptop, or Android Phone with SEELab3 software

### 3. Theory & Principle

A lemon acts as an electrolyte. Two dissimilar metals inserted into the lemon form a galvanic cell.  
The open-circuit voltage (EMF) depends on the electrode pair and electrolyte condition.

For this experiment, use one channel (`A1` or `A3`) and measure with respect to `GND`.

Expected EMF trend follows metal reactivity difference:
- larger reactivity difference -> higher EMF
- copper is commonly used as the positive electrode in these pairs

Always measure voltage with respect to `GND`:
$$
V_{\text{measured}} = V(\text{Input}) - V(\text{GND})
$$

### 4. Circuit Diagram / Setup

1. Select one input channel (`A1` recommended; `A3` is also fine here).
2. Insert two different metal electrodes into the lemon, separated by ~2-3 cm.
3. Connect the electrode expected to be negative (e.g., zinc) to `GND`.
4. Connect the other electrode (e.g., copper) to the selected input.
5. Open DC voltage measurement in the SEELab software/app.

### 5. Procedure

1. Start with the **Zn-Cu** pair and note the voltage.
2. Swap leads once and confirm sign reversal.
3. Repeat with other pairs (Fe-Cu, Al-Cu, Zn-Fe, etc.).
4. For each pair, wait 5-10 seconds for reading to stabilize and record value.
5. Optional: connect two lemon cells in series and verify voltage addition.


<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 28%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/GetStart/images/lemoncell-screen-phone.jpg" alt=" Mobile App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Mobile App</p>
    </div>
    <div class="image-column" style="flex: 0 0 68%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/GetStart/images/lemoncell-screen-desktop.jpg" alt=" Desktop App" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Desktop App</p>
    </div>
  </div>
</div>

<img src="/assets/img/seelab/GetStart/images/mangocell-setup-eyes17.jpg" alt=" Mobile App" style="width: 60%; height: auto; border: 1px solid #eee;">

### 6. Observation Table

| Metal Pair | Typical EMF Range in Lemon (V) | Measured Voltage (V) | Remarks |
| :--- | :--- | :--- | :--- |
| Zn-Cu | 0.8 to 1.1 | | |
| Al-Cu | 0.6 to 1.0 | | |
| Fe-Cu | 0.4 to 0.8 | | |
| Zn-Fe | 0.2 to 0.5 | | |
| Al-Fe | 0.1 to 0.4 | | |

### 7. Reference EMF Values (Common Metals)

Approximate standard electrode potentials (vs SHE, at 25 C):

| Metal / Electrode | $E^\circ$ (V) |
| :--- | :---: |
| Zn / Zn$^{2+}$ | -0.76 |
| Al / Al$^{3+}$ | -1.66 |
| Fe / Fe$^{2+}$ | -0.44 |
| Cu / Cu$^{2+}$ | +0.34 |

Approximate ideal EMF for common pairs (difference of $E^\circ$):

| Pair (Anode-Cathode) | Ideal $\Delta E^\circ$ (V) |
| :--- | :---: |
| Al-Cu | 2.00 |
| Zn-Cu | 1.10 |
| Fe-Cu | 0.78 |
| Al-Fe | 1.22 |
| Zn-Fe | 0.32 |

In real lemon cells, measured values are usually lower due to internal resistance, polarization, oxide layers, and non-standard ion concentrations.

### 8. Advanced: Estimating Internal Resistance of Lemon Cell

Model the lemon cell as an ideal source $E$ in series with internal resistance $r$.

When connected to a voltmeter of input resistance $R_{in}$, measured terminal voltage is:
$$
V = E\cdot\frac{R_{in}}{r+R_{in}}
$$

For this experiment:
- A1 input resistance $R_{A1}\approx1M\Omega$
- A3 input resistance $R_{A3}\approx10M\Omega$

#### Steps
1. Build one lemon cell (for example Zn-Cu).
2. Measure open terminal voltage with A1: call it $V_{A1}$.
3. Measure same cell with A3: call it $V_{A3}$.
4. Use the formula below to estimate $r$.

From two readings:
$$
r=\frac{R_{A1}R_{A3}(V_{A3}-V_{A1})}{V_{A1}R_{A3}-V_{A3}R_{A1}}
$$

Then estimate EMF:
$$
E=V_{A1}\left(1+\frac{r}{R_{A1}}\right)
$$

#### Worked Example
Suppose measured values are:
- $V_{A1}=0.60V$
- $V_{A3}=0.90V$

Using $R_{A1}=1M\Omega$, $R_{A3}=10M\Omega$:
$$
r=\frac{(1)(10)(0.90-0.60)}{(0.60)(10)-(0.90)(1)}M\Omega
=\frac{3}{5.1}M\Omega\approx0.588M\Omega
$$

So internal resistance is about:
$$
r\approx5.9\times10^5\Omega
$$

Now EMF:
$$
E\approx0.60\left(1+\frac{0.588}{1}\right)\approx0.95V
$$

### 9. Error Analysis

Possible causes of small mismatch:
* **Electrode surface condition:** rust/oxide layer reduces effective EMF.
* **Electrolyte variability:** acidity differs from lemon to lemon.
* **Internal resistance:** lemon cell has high internal resistance, especially under load.
* **Input loading:** A3 (about $10M\Omega$) disturbs weak sources less than A1/A2 (about $1M\Omega$).

### 10. Results and Discussion

* Different metal pairs produced different EMF values.
* Pairs with larger reactivity difference generally gave higher voltage (e.g., Zn-Cu > Zn-Fe).
* For two lemon cells in series, total voltage approximately added:
  $$
  V_{\text{total}} \approx V_1 + V_2
  $$

### 11. Precautions

1. Keep electrode tips clean for repeatable readings.
2. Do not let electrodes touch each other inside the lemon.
3. Use common `GND` reference and firm connections.

### 12. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| **Reading near 0V** | Same metal used / short / wrong wiring | Use dissimilar metals; recheck `GND` and input wiring |
| **Unstable reading** | Loose clips / dry lemon region | Reinsert electrodes, moisten area, tighten contacts |
| **Too low voltage** | Oxidized electrodes / weak acidity | Clean electrodes and try fresh lemon |
| **Wrong polarity sign** | Leads reversed | Swap electrode connections |

<div class="viva-section nosplit">

<h3> 13. Viva-Voce Questions </h3>

<details>
<summary><b>Q1. Why does a lemon cell produce voltage?</b></summary>
<p>
<b>Ans:</b> Two dissimilar metals in an electrolyte form an electrochemical cell. Their different electrode potentials create an EMF.
</p>
</details>

<details>
<summary><b>Q2. Why is Zn-Cu usually higher than Zn-Fe in a lemon cell?</b></summary>
<p>
<b>Ans:</b> The electrode potential difference for Zn-Cu is larger than Zn-Fe, so EMF is generally higher.
</p>
</details>

<details>
<summary><b>Q3. Why are measured lemon-cell voltages lower than ideal EMF values?</b></summary>
<p>
<b>Ans:</b> Due to internal resistance, polarization, oxide layers, and non-standard chemical conditions.
</p>
</details>

<details>
<summary><b>Q4. If a 3V source is connected to A1 through a 1M&Omega; resistor, what is the displayed voltage (A1 input impedance = 1M&Omega;)?</b></summary>
<p>
<b>Ans:</b> Using voltage divider:
$$
V_{A1}=3\times\frac{1}{1+1}=1.5V
$$
Displayed value is approximately <b>1.5V</b>.
</p>
</details>

<details>
<summary><b>Q5. For the same setup, what is displayed on A3 (input impedance = 10M&Omega;)?</b></summary>
<p>
<b>Ans:</b>
$$
V_{A3}=3\times\frac{10}{1+10}=3\times\frac{10}{11}\approx2.73V
$$
A3 shows approximately <b>2.73V</b>.
</p>
</details>

</div>