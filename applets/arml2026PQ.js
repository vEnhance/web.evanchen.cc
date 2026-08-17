"use strict";

// ── Factoring ─────────────────────────────────────────────────────────────────

const FACTOR_LIMIT = 1_000_000n;

// Trial-divide n into prime factors. Returns { factors: Map<BigInt,BigInt> }
// or { err } if n has a prime factor that would require p > FACTOR_LIMIT to find.
function trialDivide(n) {
  const factors = new Map();
  if (n <= 1n) return { factors };

  let rem = n;

  while (rem % 2n === 0n) {
    factors.set(2n, (factors.get(2n) ?? 0n) + 1n);
    rem /= 2n;
  }

  for (let p = 3n; p * p <= rem; p += 2n) {
    if (p > FACTOR_LIMIT) return { err: "too large to factor" };
    while (rem % p === 0n) {
      factors.set(p, (factors.get(p) ?? 0n) + 1n);
      rem /= p;
    }
  }

  if (rem > 1n) factors.set(rem, (factors.get(rem) ?? 0n) + 1n);

  return { factors };
}

// Parse an expression like "9 * 10^8" or "2^3 * 3 * 5" into the prime
// factorization of the resulting integer.
// Returns { primes: [{p, e}, ...] sorted by p } or { err }.
function evalExpr(raw) {
  const s = raw.replace(/\s+/g, "");
  if (!s) return { primes: [] };

  const acc = new Map(); // prime → accumulated exponent

  for (const term of s.split("*")) {
    if (!term) return { err: "empty term after ×" };

    const parts = term.split("^");
    if (parts.length > 2) return { err: `too many ^ in "${term}"` };

    let base, termExp;
    try {
      base = BigInt(parts[0]);
      termExp = parts.length === 2 ? BigInt(parts[1]) : 1n;
    } catch {
      return { err: `cannot parse "${term}"` };
    }

    if (base < 1n) return { err: "value must be ≥ 1" };
    if (termExp < 0n) return { err: "exponent must be ≥ 0" };
    if (base === 1n || termExp === 0n) continue; // multiplying by 1

    const { factors, err } = trialDivide(base);
    if (err) return { err };

    for (const [p, e] of factors) {
      acc.set(p, (acc.get(p) ?? 0n) + e * termExp);
    }
  }

  const primes = [...acc.entries()]
    .sort(([a], [b]) => (a < b ? -1 : 1))
    .map(([p, e]) => ({ p, e }));

  return { primes };
}

// ── Math ──────────────────────────────────────────────────────────────────────

function gcd(a, b) {
  if (a < 0n) a = -a;
  if (b < 0n) b = -b;
  while (b) [a, b] = [b, a % b];
  return a;
}

// A(n) = σ(n)/n = ∏ (p^(e+1) - 1) / ((p-1) · p^e)
function sigmaRatio(primes) {
  let num = 1n,
    den = 1n;
  for (const { p, e } of primes) {
    const pe = p ** e;
    num *= p * pe - 1n;
    den *= (p - 1n) * pe;
  }
  const g = gcd(num, den);
  return [num / g, den / g];
}

function toDecimalStr(num, den) {
  const SCALE = 10_000_000n;
  const q = Number((num * SCALE) / den) / 1e7;
  if (!isFinite(q)) return null;
  return parseFloat(q.toFixed(6)).toString();
}

function computeN(primes) {
  let n = 1n;
  for (const { p, e } of primes) n *= p ** e;
  return n;
}

function formatN(n) {
  const s = n.toString();
  if (s.length <= 12) return s.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return `${s[0]}.${s.slice(1, 4)}×10^${s.length - 1}`;
}

// ── HTML rendering helpers ────────────────────────────────────────────────────

function facHTML(primes) {
  return primes
    .map(({ p, e }) => {
      const b = String(p);
      return e === 1n ? b : `${b}<sup>${e}</sup>`;
    })
    .join(" · ");
}

function ratioHTML(num, den) {
  if (den === 1n) return String(num);
  return `<span class="vfrac"><span class="vfrac-num">${num}</span><span class="vfrac-den">${den}</span></span>`;
}

// ── UI ────────────────────────────────────────────────────────────────────────

const input = document.getElementById("expr");
const outN = document.getElementById("out-n");
const outFac = document.getElementById("out-fac");
const outRatio = document.getElementById("out-ratio");
const outDec = document.getElementById("out-dec");
const eq2 = document.getElementById("eq2");

function render() {
  const raw = input.value;

  if (!raw.trim()) {
    outN.textContent = "…";
    outFac.innerHTML = "";
    eq2.style.visibility = "hidden";
    outRatio.innerHTML = "…";
    outDec.textContent = "";
    return;
  }

  const result = evalExpr(raw);

  if (result.err) {
    outN.textContent = result.err;
    outFac.innerHTML = "";
    eq2.style.visibility = "hidden";
    outRatio.innerHTML = "…";
    outDec.textContent = "";
    return;
  }

  const { primes } = result;
  const n = computeN(primes);

  outN.textContent = formatN(n);

  if (primes.length > 0) {
    outFac.innerHTML = facHTML(primes);
    eq2.style.visibility = "visible";
  } else {
    // n = 1: no prime factorization row
    outFac.innerHTML = "";
    eq2.style.visibility = "hidden";
  }

  const [num, den] = sigmaRatio(primes);
  outRatio.innerHTML = ratioHTML(num, den);
  outDec.textContent = den !== 1n ? `≈ ${toDecimalStr(num, den) ?? ""}` : "";
}

// ── Keypad ────────────────────────────────────────────────────────────────────

document.getElementById("keypad").addEventListener("pointerdown", (e) => {
  const btn = e.target.closest("[data-k]");
  if (!btn) return;
  e.preventDefault(); // keep focus on input; suppress soft keyboard on mobile

  btn.classList.add("pressed");
  setTimeout(() => btn.classList.remove("pressed"), 120);

  input.focus();

  const k = btn.dataset.k;

  if (k === "enter") {
    render();
    return;
  }

  if (k === "clear") {
    input.value = "";
    render();
    return;
  }

  const v = input.value;
  const sel0 = input.selectionStart ?? v.length;
  const sel1 = input.selectionEnd ?? sel0;

  let newV, pos;
  if (k === "back") {
    if (sel0 !== sel1) {
      newV = v.slice(0, sel0) + v.slice(sel1);
      pos = sel0;
    } else if (sel0 > 0) {
      newV = v.slice(0, sel0 - 1) + v.slice(sel0);
      pos = sel0 - 1;
    } else {
      return;
    }
  } else {
    const ins = k === "*" ? " * " : k;
    newV = v.slice(0, sel0) + ins + v.slice(sel1);
    pos = sel0 + ins.length;
  }

  input.value = newV;
  input.setSelectionRange(pos, pos);
  render();
});

input.addEventListener("input", render);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") render();
});

window.addEventListener("load", () => input.focus());
