---
layout: editmanual
title: "Edit Manuals"
description: Edit and preview SEELab manual body text
permalink: /printmanual/
search: exclude
---

<style>
:root {
        --primary-blue: #004a99;
        --accent-gray: #f4f4f4;
        --text-main: #333;
        --border-color: #ccc;
    }

    /* Print logic */
    @media print {
        @page {
            size: A4 landscape;
            margin: 0;
        }
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            width: 100%;
            -webkit-print-color-adjust: exact; /* Ensures colors print */
        }
    }

    body {
        font-family: 'Segoe UI', sans-serif;
        margin: 0;
    }

    .a4-sheet {
        width: 297mm;
        height: 210mm;
        display: flex;
        page-break-after: always;
        page-break-inside: avoid;
        box-sizing: border-box;
        overflow: hidden; /* Prevents overflow-induced blank pages */
    }

    /* Individual A5 Panels */
    .a5-panel {
        width: 148.5mm; /* Exact half of 297mm */
        height: 100%;
        padding: 15mm;
        box-sizing: border-box; /* CRITICAL: Includes padding in width/height */
        border-right: 1px solid var(--border-color);
        position: relative;
    }

    .a5-panel:nth-child(2n) {
        border-right: none;
    }

    /* Standardized visuals */
    .img-placeholder {
        width: 100%;
        height: 140px;
        background: #e0e0e0;
        border: 2px dashed #999;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px 0;
        font-size: 0.9em;
    }

    .code-block {
        background: #222;
        color: #7cfc00;
        padding: 8px;
        font-family: 'Courier New', monospace;
        font-size: 0.75em;
        border-radius: 4px;
        white-space: pre-wrap;
    }

    table { width: 100%; border-collapse: collapse; font-size: 0.8em; }
    th, td { border: 1px solid #ddd; padding: 4px; }
    h1, h2, h3 { color: var(--primary-blue); margin: 5px 0; }
    .page-number { position: absolute; bottom: 8mm; left: 0; width: 100%; text-align: center; font-weight: bold; }
  </style>

<div class="a4-sheet">
    <div class="a5-panel">
        <h2>Support & Safety</h2>
        <p><strong>Common Troubleshooting:</strong></p>
        <ul>
            <li>Device Not Found: Check USB drivers.</li>
            <li>Noisy Signal: Ensure common ground.</li>
        </ul>
        <div class="img-placeholder">Safety Symbols / QR Codes</div>
        <p><small>Designed for educational excellence. Made for SEELab3 Users.</small></p>
        <div class="page-number">8</div>
    </div>
    
    <div class="a5-panel cover">
        <div class="img-placeholder" style="height: 250px;">SEELab3 LOGO / IMAGE</div>
        <h1>SEELab3</h1>
        <h3>User Manual & Quick Start</h3>
        <p>Exploration, Experimentation, and Programming</p>
        <div class="page-number">1</div>
    </div>
</div>

<div class="a4-sheet">
    <div class="a5-panel">
        <h2>Pin Diagrams</h2>
        <div class="img-placeholder">Hardware Top View Labeled</div>
        <table>
            <tr><th>Pin</th><th>Function</th><th>Range</th></tr>
            <tr><td>A1, A2</td><td>Analog In</td><td>+/- 10V</td></tr>
            <tr><td>IN1</td><td>Freq Counter</td><td>0-5V</td></tr>
            <tr><td>PV1</td><td>Prog. Voltage</td><td>-5 to +5V</td></tr>
        </table>
        <div class="page-number">2</div>
    </div>

    <div class="a5-panel">
        <h2>Sample Experiments</h2>
        <h3>1. Ohm's Law</h3>
        <p>Connect a resistor between PV1 and Ground. Use A1 to measure voltage drop.</p>
        <div class="img-placeholder">Circuit Schematic</div>
        <h3>2. RC Circuits</h3>
        <p>Observe capacitor charging on the Oscilloscope.</p>
        <div class="page-number">7</div>
    </div>
</div>

<div class="a4-sheet">
    <div class="a5-panel">
        <h2>Python Programming</h2>
        <p>Install the library via terminal:</p>
        <div class="code-block">pip install seelab</div>
        <p>Example Script:</p>
        <div class="code-block">
            import seelab<br>
            dev = seelab.connect()<br>
            val = dev.read_ADC(1)<br>
            print(val)
        </div>
        <div class="page-number">6</div>
    </div>

    <div class="a5-panel">
        <h2>Setup & Resources</h2>
        <h3>Installation</h3>
        <ol>
            <li>Download drivers from website.</li>
            <li>Run SEELab_Setup.exe.</li>
            <li>Connect device via USB.</li>
        </ol>
        <div class="img-placeholder">Installation Screenshot</div>
        <p><strong>Resources:</strong> github.com/seelab3</p>
        <div class="page-number">3</div>
    </div>
</div>

<div class="a4-sheet">
    <div class="a5-panel">
        <h2>Software Apps</h2>
        <p><strong>Desktop Suite:</strong> Integrated Oscilloscope, Multimeter, and Logic Analyzer.</p>
        <div class="img-placeholder">Desktop App Interface</div>
        <p><strong>Android App:</strong> Use USB-OTG or Bluetooth to monitor sensors on the go.</p>
        <div class="page-number">4</div>
    </div>

    <div class="a5-panel">
        <h2>Visual Coding</h2>
        <p>Use Blockly to drag-and-drop logic for hardware control.</p>
        <div class="img-placeholder">Blockly Workspace Example</div>
        <p>Great for beginners to learn loops, logic, and I/O control.</p>
        <div class="page-number">5</div>
    </div>
</div>
