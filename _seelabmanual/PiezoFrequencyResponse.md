---
layout: manual
title: "Frequency Response of Piezo Buzzer"
date: 31 March 2026
image:
  path: /assets/img/seelab/sound/images/freq-resp-setup.jpg
caption: Piezo buzzer frequency sweep and microphone response measurement
section: Acoustics
---

## Experiment: Frequency Response of Piezo Buzzer

### 1. Aim

To measure acoustic output versus drive frequency of a piezo buzzer and identify its resonant frequency region.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* Piezo buzzer
* Microphone/sound sensor
* Connecting wires
* Data capture interface

---

### 3. Theory & Principle

Piezo buzzers show non-uniform response with frequency. Output intensity peaks near mechanical resonance determined by buzzer structure and enclosure.

By sweeping frequency and measuring microphone amplitude, we obtain response curve:

$$A = f(\nu)$$

Peak of this curve corresponds to resonance frequency.

---

### 4. Circuit Diagram / Setup

1. Connect piezo buzzer to waveform output.
2. Place microphone at fixed distance from buzzer.
3. Ensure constant geometry during sweep.
4. Open frequency-response measurement screen.

---

### 5. Procedure

1. Set sweep range (e.g., 1 kHz to 5 kHz).
2. Run sweep and record microphone amplitude at each step.
3. Plot amplitude vs frequency.
4. Identify resonance peak and bandwidth around peak.
5. Repeat once for consistency check.

<img src="/assets/img/seelab/sound/images/freq-resp-screen-phone.jpg" style="width: 38%; display: block; margin: 20px auto; border: 1px solid #eee;">

---

### 6. Observation Table

| Frequency (Hz) | Amplitude (arb.) |
| :---: | :---: |
| 1000 | |
| 1500 | |
| 2000 | |
| 2500 | |
| 3000 | |
| 3500 | |
| 4000 | |
| 4500 | |
| 5000 | |

---

### 7. Results and Discussion

* Frequency response was non-uniform as expected.
* Peak response occurred near ________ Hz (resonant zone).
* Away from resonance, output amplitude dropped significantly.

---

### 8. Precautions

1. Keep microphone distance fixed throughout sweep.
2. Avoid reflections from nearby hard surfaces where possible.
3. Use same gain settings for all readings.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| Flat response curve | Microphone clipping/low sensitivity | Adjust mic gain and verify connection |
| Irregular spikes | Environmental noise/reflections | Repeat in quieter open area |
| No clear resonance | Defective buzzer or too narrow sweep | Expand sweep range and test buzzer |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why can't ExpEYES directly drive an 8 Ohm loudspeaker from sine output?</b></summary><p><b>Ans:</b> The source cannot supply the high current demanded by low-impedance loads; piezo is a higher-impedance alternative.</p></details>
<details><summary><b>Q2. What is resonant frequency in this context?</b></summary><p><b>Ans:</b> Frequency at which buzzer mechanical-electrical coupling gives maximum output amplitude.</p></details>
</div>

