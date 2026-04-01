---
layout: manual
title: "Interference of Sound (Beats)"
date: 31 March 2026
image:
  path: /assets/img/seelab/sound/images/beats-setup.jpg
caption: Two-buzzer setup for beat formation and envelope observation
section: Acoustics
---

## Experiment: Interference of Sound (Beats)

### 1. Aim

To observe acoustic beats formed by superposition of two nearby frequencies and verify that beat frequency equals frequency difference.

---

### 2. Apparatus / Components Required

* SEELab3 unit
* Two piezo buzzers
* Microphone module
* Mounting wire/support for microphone near I2C socket
* Connecting wires

---

### 3. Theory & Principle

When two sinusoidal waves of close frequencies $f_1$ and $f_2$ superpose, the resultant amplitude varies slowly, producing beats.

$$f_{beat} = |f_1 - f_2|$$

In this setup, typical drive values are around:

* buzzer 1: 3300 Hz sine
* buzzer 2: 3400 Hz square/sine

Expected beat frequency is approximately 100 Hz.

---

### 4. Circuit Diagram / Setup

1. Connect both buzzers to signal outputs as per ExpEYES arrangement.
2. Place microphone between/near the two buzzers and secure mechanically.
3. Adjust relative distances to maximize envelope visibility.
4. Capture waveform and FFT using SEELab interface.

---

### 5. Procedure

1. Set two close but distinct frequencies.
2. Start acquisition and observe amplitude modulation envelope.
3. Measure time between successive envelope maxima to get beat period $T_b$.
4. Compute beat frequency:

$$f_{beat}=\frac{1}{T_b}$$

5. Verify against $|f_1-f_2|$.
6. Open FFT and confirm both source frequency peaks are present.

<div class="nosplit">
  <div class="image-row" style="display: flex; flex-wrap: nowrap; gap: 20px; margin: 20px 0; justify-content: center; width: 100%;">
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/sound/images/beats-screen-phone.jpg" alt="Beats waveform screen" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">Waveform with Beat Envelope</p>
    </div>
    <div class="image-column" style="flex: 0 0 48%; text-align: center; box-sizing: border-box;">
      <img src="/assets/img/seelab/sound/images/beats-fft-screen-phone.jpg" alt="Beats FFT screen" style="width: 100%; height: auto; border: 1px solid #eee;">
      <p class="caption" style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">FFT showing both components</p>
    </div>
  </div>
</div>

---

### 6. Observation Table

| Trial | $f_1$ (Hz) | $f_2$ (Hz) | Predicted $|f_1-f_2|$ (Hz) | Measured $f_{beat}$ (Hz) | Error (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

---

### 7. Results and Discussion

* Clear beat envelope was observed for nearby frequencies.
* Measured beat frequency matched $|f_1-f_2|$ within experimental error.
* FFT confirmed coexistence of two close frequency components.

---

### 8. Precautions

1. Keep frequencies close (difference ~50-200 Hz) for visible beats.
2. Adjust microphone position to avoid near-field null points.
3. Avoid ambient noise and table vibrations during measurement.

---

### 9. Troubleshooting

| Symptom | Possible Cause | Corrective Action |
| :--- | :--- | :--- |
| No clear beats | Frequency difference too large/small | Set closer frequencies |
| Very weak envelope | Poor microphone placement | Reposition mic between sources |
| FFT shows one peak only | One source not connected | Verify both buzzer channels |

---

<div class="viva-section nosplit">
<h3>10. Viva-Voce Questions</h3>
<details><summary><b>Q1. Why do beats occur?</b></summary><p><b>Ans:</b> Due to constructive and destructive interference between two close frequencies.</p></details>
<details><summary><b>Q2. Why is beat frequency not equal to average frequency?</b></summary><p><b>Ans:</b> Average frequency gives carrier oscillation, while beat frequency is the envelope rate ($|f_1-f_2|$).</p></details>
</div>

