---
layout: manual
title: "NPN Common-Emitter Output (Python / eyes17)"
date: 10 April 2026
image:
  path: /assets/img/seelab/electronics/images/transistorCE-setup-seelab3.jpg
caption: CE output setup — PV1 + R_C at collector (A1), PV2 + R_B at base (A2), emitter to GND
section: Interfacing
---

## NPN CE output via Python (`eyes17`)

This unit drives **PV1** (collector sweep through $R_C$), **PV2** (base bias through $R_B = 100\,\text{k}\Omega$), reads **A1** / **A2**, and plots **$I_C$ vs $V_{CE}$** using the **`eyes17`** API. For theory, tables, and precautions, see [Output Characteristics of an NPN Transistor](/manual/NPNOutput/).

---

### 1. Aim

To script the **common-emitter output characteristic**: sweep **PV1** at a set **PV2**, compute $I_C$ and $V_{CE}$, and plot the curve. The interactive example uses a **slider** only to change **PV2** (and show $I_B$), plus **Acquire** to run a sweep and **Clear all** to remove traces.

---

### 2. Requirements

* SEELab3 / ExpEYES-17 (needs **PV1**, **PV2**, **A1**, **A2**)
* Python 3 with **`eyes17`**, **`matplotlib`**, **`numpy`**
* 2N2222 (or similar NPN), $R_C = 1\,\text{k}\Omega$, $R_B = 100\,\text{k}\Omega$

**Wiring** (same as the main manual):

1. **PV2** → $R_B$ → **base**; **A2** at the base node.
2. **PV1** → $R_C$ → **collector**; **A1** at the collector node.
3. **Emitter** → **GND**.

**Currents** (voltages in V, resistors in $\Omega$):

$$I_B = \frac{V_{\text{PV2}} - V_{\text{A2}}}{R_B}, \qquad I_C = \frac{V_{\text{PV1}} - V_{\text{A1}}}{R_C}$$

With emitter grounded, **$V_{CE} \approx V_{\text{A1}}$**. Display $I_B$ in $\mu\text{A}$: multiply by $10^6$.

---

### 3. Simple example — fixed PV2, one $I_C$–$V_{CE}$ sweep

```python
import numpy as np
import eyes17.eyes
import matplotlib.pyplot as plt

p = eyes17.eyes.open()
RC = 1000.0
RB = 100_000.0
PV2_BIAS = 1.5  # V; tune for desired I_B (order of a few µA to tens of µA)

p.set_pv2(PV2_BIAS)
import time
time.sleep(0.05)

vce_v = []
ic_ma = []

for v_pv1 in np.arange(0.0, 3.36, 0.06):
    p.set_pv1(float(v_pv1))
    time.sleep(0.02)
    va1 = p.get_voltage("A1")
    vce_v.append(va1)
    ic_ma.append((v_pv1 - va1) / RC * 1000.0)

va2 = p.get_voltage("A2")
ib_ua = (PV2_BIAS - va2) / RB * 1e6

p.set_pv1(0.0)

plt.xlabel("V_CE (V)")
plt.ylabel("I_C (mA)")
plt.title(f"NPN CE output  (PV2 = {PV2_BIAS} V,  I_B ≈ {ib_ua:.1f} µA)")
plt.grid(True)
plt.plot(vce_v, ic_ma, "b-o", markersize=3)
plt.show()
```

---

### 4. Interactive demo — **Slider** = PV2 only; **Acquire** / **Clear** buttons

The **slider** only updates **PV2** (base bias) and refreshes an **$I_B$** estimate from **A2** — it does **not** sweep PV1. Press **Acquire trace** to run one **PV1** sweep and append an **$I_C$–$V_{CE}$** curve at the current PV2. **Clear all** removes every acquired trace from the plot.

```python
import time

import numpy as np
import eyes17.eyes
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

p = eyes17.eyes.open()
RC = 1000.0
RB = 100_000.0

fig, ax = plt.subplots(figsize=(10, 6.5))
plt.subplots_adjust(bottom=0.28)

ax.set_xlim(0, 3.5)
ax.set_ylim(0, 3.5)
ax.set_xlabel("V_CE (V)  [≈ voltage at A1]")
ax.set_ylabel("I_C (mA)")
ax.set_title("NPN CE — slider = PV2 only; Acquire = PV1 sweep")
ax.grid(True)

traces = []

ax_sl = plt.axes([0.12, 0.16, 0.56, 0.03])
slider = Slider(ax_sl, "PV2 (V)", 1.0, 3.2, valinit=1.5, valstep=0.05)

status = fig.text(0.12, 0.11, "", fontsize=9, family="sans-serif")


def refresh_pv2_display(_val=None):
    vv = float(slider.val)
    p.set_pv2(vv)
    time.sleep(0.03)
    va2 = p.get_voltage("A2")
    ib_ua = (vv - va2) / RB * 1e6
    status.set_text(f"PV2 = {vv:.2f} V  |  I_B ≈ {ib_ua:.2f} µA  (no sweep yet — press Acquire)")
    fig.canvas.draw_idle()


def on_slider_change(_val):
    refresh_pv2_display()


slider.on_changed(on_slider_change)
refresh_pv2_display()


def acquire_trace(_event):
    v_pv2 = float(slider.val)
    p.set_pv2(v_pv2)
    time.sleep(0.05)

    vce_list = []
    ic_list = []
    for v_pv1 in np.arange(0.0, 3.36, 0.08):
        p.set_pv1(float(v_pv1))
        time.sleep(0.02)
        va1 = p.get_voltage("A1")
        vce_list.append(va1)
        ic_list.append((v_pv1 - va1) / RC * 1000.0)

    va2 = p.get_voltage("A2")
    ib_ua = (v_pv2 - va2) / RB * 1e6

    (new_line,) = ax.plot(
        vce_list,
        ic_list,
        "-o",
        markersize=3,
        label=f"PV2={v_pv2:.2f} V, I_B≈{ib_ua:.1f} µA",
    )
    traces.append(new_line)
    ax.legend(fontsize=8, loc="upper left")
    p.set_pv1(0.0)
    fig.canvas.draw_idle()


def clear_traces(_event):
    for ln in traces:
        ln.remove()
    traces.clear()
    leg = ax.get_legend()
    if leg is not None:
        leg.remove()
    ax.set_xlim(0, 3.5)
    ax.set_ylim(0, 3.5)
    fig.canvas.draw_idle()


ax_acq = plt.axes([0.12, 0.045, 0.22, 0.06])
ax_clr = plt.axes([0.62, 0.045, 0.22, 0.06])
btn_acq = Button(ax_acq, "Acquire trace", color="lightsteelblue", hovercolor="steelblue")
btn_clr = Button(ax_clr, "Clear all", color="tomato", hovercolor="red")
btn_acq.on_clicked(acquire_trace)
btn_clr.on_clicked(clear_traces)


def shutdown():
    p.set_pv1(0.0)
    p.set_pv2(0.0)


fig.canvas.mpl_connect("close_event", lambda _ev: shutdown())
plt.show()
```

---

### 5. Notes

* **PV1 limit:** Keep the sweep upper bound within the safe range for your unit (often **≈ 5 V** on SEELab3 for this experiment — see the [written CE manual](/manual/NPNOutput/)).
* **PV2 range:** Too low → cut-off ($I_C \approx 0$); too high → excessive $I_B$ and $I_C$. Stay within the same safe currents as the written manual (order of **µA** base current for a 2N2222 with $100\,\text{k}\Omega$).
* **Slider vs Acquire:** Moving the slider only calls **`set_pv2`** and updates the **$I_B$** readout; **Acquire trace** is what runs the **PV1** sweep and adds a curve (build a family of curves by changing PV2 and acquiring again).
* **Cleanup:** The example zeros **PV1** and **PV2** when the figure window closes.
