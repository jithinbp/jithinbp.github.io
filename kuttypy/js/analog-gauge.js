/**
 * Semicircle analog gauge — needle and value arc share the same polar angles.
 */

const CX = 100;
const CY = 92;
const R = 72;
const NEEDLE_R = R - 10;
/** Math-style degrees: 0=right, 90=down; arc runs along the bottom 270°. */
const START = 135;
const SWEEP = 270;

function polar(angleDeg, radius = R) {
  const rad = (angleDeg * Math.PI) / 180;
  return {
    x: CX + radius * Math.cos(rad),
    y: CY + radius * Math.sin(rad),
  };
}

function arcPath(r, a0, a1) {
  if (a1 <= a0) return '';
  const p0 = polar(a0, r);
  const p1 = polar(a1, r);
  const large = a1 - a0 > 180 ? 1 : 0;
  return `M ${p0.x} ${p0.y} A ${r} ${r} 0 ${large} 1 ${p1.x} ${p1.y}`;
}

function formatValue(v, lo, hi) {
  const span = Math.abs(hi - lo);
  if (span < 1) return v.toFixed(3);
  if (span < 20) return v.toFixed(2);
  if (span < 200) return v.toFixed(1);
  return Math.round(v).toString();
}

export function createAnalogGauge(label, unit, min, max) {
  const uid = `g${Math.random().toString(36).slice(2, 9)}`;
  const root = document.createElement('div');
  root.className = 'analog-gauge';
  root.innerHTML = `
    <div class="gauge-face" aria-hidden="true">
      <svg viewBox="0 0 200 118" class="gauge-svg">
        <defs>
          <linearGradient id="${uid}-track" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1e3a5f"/>
            <stop offset="50%" stop-color="#334155"/>
            <stop offset="100%" stop-color="#1e3a5f"/>
          </linearGradient>
          <linearGradient id="${uid}-fill" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#0ea5e9"/>
            <stop offset="55%" stop-color="#38bdf8"/>
            <stop offset="100%" stop-color="#22d3ee"/>
          </linearGradient>
          <filter id="${uid}-glow" x="-40%" y="-40%" width="180%" height="180%">
            <feGaussianBlur stdDeviation="2" result="b"/>
            <feMerge>
              <feMergeNode in="b"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        <path class="gauge-track" d="${arcPath(R, START, START + SWEEP)}" stroke="url(#${uid}-track)"/>
        <path class="gauge-value-arc" d="" stroke="url(#${uid}-fill)" filter="url(#${uid}-glow)"/>
        <g class="gauge-ticks"></g>
        <circle class="gauge-hub-outer" cx="${CX}" cy="${CY}" r="9"/>
        <circle class="gauge-hub" cx="${CX}" cy="${CY}" r="5.5"/>
        <line class="gauge-needle" x1="${CX}" y1="${CY}" x2="${CX}" y2="${CY}"/>
      </svg>
    </div>
    <div class="gauge-readout">
      <span class="gauge-label">${label}</span>
      <div class="gauge-value-row">
        <span class="gauge-value">—</span>
        <span class="gauge-unit">${unit}</span>
      </div>
      <span class="gauge-range"></span>
    </div>
  `;

  const ticksG = root.querySelector('.gauge-ticks');
  const valueArc = root.querySelector('.gauge-value-arc');
  const needle = root.querySelector('.gauge-needle');
  const labelEl = root.querySelector('.gauge-label');
  const valueEl = root.querySelector('.gauge-value');
  const rangeEl = root.querySelector('.gauge-range');
  let lo = min;
  let hi = max;

  function buildTicks() {
    ticksG.innerHTML = '';
    const majors = 5;
    for (let i = 0; i <= majors; i++) {
      const t = i / majors;
      const angle = START + t * SWEEP;
      const outer = polar(angle, R + 2);
      const inner = polar(angle, R - (i % majors === 0 ? 10 : 5));
      const tick = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      tick.setAttribute('x1', inner.x);
      tick.setAttribute('y1', inner.y);
      tick.setAttribute('x2', outer.x);
      tick.setAttribute('y2', outer.y);
      tick.setAttribute('class', i === 0 || i === majors ? 'gauge-tick-major' : 'gauge-tick-minor');
      ticksG.appendChild(tick);

      if (i === 0 || i === majors || i === Math.floor(majors / 2)) {
        const val = lo + t * (hi - lo);
        const lp = polar(angle, R - 18);
        const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        text.setAttribute('x', lp.x);
        text.setAttribute('y', lp.y);
        text.setAttribute('class', 'gauge-tick-label');
        text.setAttribute('text-anchor', 'middle');
        text.setAttribute('dominant-baseline', 'middle');
        text.textContent = formatValue(val, lo, hi);
        ticksG.appendChild(text);
      }
    }
    rangeEl.textContent = `${formatValue(lo, lo, hi)} – ${formatValue(hi, lo, hi)} ${unit}`;
  }

  function setRange(minVal, maxVal) {
    lo = Number(minVal);
    hi = Number(maxVal);
    if (!Number.isFinite(lo) || !Number.isFinite(hi) || lo === hi) {
      hi = lo + 1;
    }
    buildTicks();
  }

  function valueToAngle(v) {
    const clamped = Math.max(lo, Math.min(hi, v));
    const t = (clamped - lo) / (hi - lo);
    return START + t * SWEEP;
  }

  function setNeedle(angleDeg) {
    const tip = polar(angleDeg, NEEDLE_R);
    needle.setAttribute('x1', CX);
    needle.setAttribute('y1', CY);
    needle.setAttribute('x2', tip.x);
    needle.setAttribute('y2', tip.y);
  }

  function update(value) {
    const v = Number(value);
    if (!Number.isFinite(v)) {
      valueEl.textContent = '—';
      valueArc.setAttribute('d', '');
      setNeedle(START);
      return;
    }
    const angle = valueToAngle(v);
    valueArc.setAttribute('d', arcPath(R - 6, START, angle));
    setNeedle(angle);
    valueEl.textContent = formatValue(v, lo, hi);
  }

  setRange(min, max);
  update(NaN);

  function setLabel(text) {
    labelEl.textContent = text;
  }

  return { el: root, update, setRange, setLabel };
}
