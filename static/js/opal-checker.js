// Client-side grading and hints for the OPAL archive page.
// The opal() macro emits, for each hunt, a <script type="application/json"
// class="opal-data"> blob alongside the <ol> it describes; this script reads
// those, checks submitted answers against the salted hashes, remembers solves
// in localStorage, and reveals rot13'd hints one at a time.

const SALT = "opal_puzzle_hunt_secret_salt";
const STORAGE_KEY = "opal-solved";

function normalizeAnswer(answer) {
  // Keep only alphanumeric characters and convert to lowercase
  return answer.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
}

async function hashAnswer(normalizedAnswer) {
  // Hash the normalized answer with salt using SHA-256
  const saltedAnswer = normalizedAnswer + SALT;
  const encoder = new TextEncoder();
  const data = encoder.encode(saltedAnswer);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);

  // Convert buffer to hex string
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
  return hashHex;
}

// Hint text comes out of otis-web in a light markdown; render the two bits of
// it that actually turn up, `code` and _emphasis_, instead of showing the
// punctuation. Everything else stays plain text.
function appendInline(parent, text) {
  const pattern = /`([^`]+)`|_([^_]+)_/g;
  let last = 0;
  let match;
  while ((match = pattern.exec(text)) !== null) {
    parent.append(text.slice(last, match.index));
    const code = match[1] !== undefined;
    const el = document.createElement(code ? "code" : "em");
    el.textContent = code ? match[1] : match[2];
    parent.append(el);
    last = pattern.lastIndex;
  }
  parent.append(text.slice(last));
}

function rot13(text) {
  return text.replace(/[a-zA-Z]/g, (c) => {
    const base = c <= "Z" ? 65 : 97;
    return String.fromCharCode(((c.charCodeAt(0) - base + 13) % 26) + base);
  });
}

// ---------------------------------------------------------------------------
// Puzzle data
// ---------------------------------------------------------------------------

function loadPuzzles() {
  const puzzles = [];
  for (const blob of document.querySelectorAll("script.opal-data")) {
    const hunt = blob.dataset.hunt;
    const label = blob.dataset.label || hunt;
    const list = document.querySelector(`ol.opal-list[data-hunt="${hunt}"]`);
    JSON.parse(blob.textContent).forEach((puzzle, i) => {
      puzzles.push({
        hunt: hunt,
        label: label,
        index: i + 1,
        title: puzzle.title,
        answerHash: puzzle.answer_hash,
        partialHashes: puzzle.partial_hashes || [],
        hints: puzzle.hints_rot13 || [],
        li: list ? list.querySelector(`li[data-index="${i + 1}"]`) : null,
      });
    });
  }
  return puzzles;
}

function loadSolved() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
  } catch {
    return {};
  }
}

function saveSolved(solved) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(solved));
  } catch {
    // e.g. private browsing; the solve still shows until the page is reloaded
  }
}

// Write a "Solved: ANSWER" line under every puzzle the visitor has cracked,
// and take it away from the ones they haven't.
function renderSolved(puzzles, solved) {
  for (const puzzle of puzzles) {
    if (!puzzle.li) continue;
    const answer = solved[puzzle.answerHash];
    let note = puzzle.li.querySelector(".opal-solved");
    if (!answer) {
      if (note) note.remove();
      continue;
    }
    if (!note) {
      note = document.createElement("div");
      note.className = "opal-solved";
      note.append("Solved: ");
      const span = document.createElement("span");
      span.className = "opal-answer";
      note.append(span);
      puzzle.li.append(note);
    }
    note.querySelector(".opal-answer").textContent = answer;
  }
}

// ---------------------------------------------------------------------------
// Answer checker
// ---------------------------------------------------------------------------

function setupChecker(puzzles, solved) {
  const input = document.getElementById("answerInput");
  const button = document.getElementById("submitButton");
  const result = document.getElementById("result");
  const reset = document.getElementById("opalReset");

  function showResult(message, kind) {
    result.textContent = message;
    result.className = `result ${kind}`;
    result.style.display = "block";
  }

  async function handleSubmit() {
    const userAnswer = input.value.trim();
    if (!userAnswer) {
      showResult("Please enter an answer", "warning");
      return;
    }

    button.disabled = true;
    button.textContent = "Checking...";
    try {
      const hash = await hashAnswer(normalizeAnswer(userAnswer));
      const solvedPuzzle = puzzles.find((p) => p.answerHash === hash);
      const partialPuzzle = puzzles.find((p) => p.partialHashes.includes(hash));
      if (solvedPuzzle) {
        solved[hash] = userAnswer.toUpperCase();
        saveSolved(solved);
        renderSolved(puzzles, solved);
        showResult(`✓ Correct! (${solvedPuzzle.title})`, "success");
        input.value = "";
      } else if (partialPuzzle) {
        showResult(`‼ Keep going! (${partialPuzzle.title})`, "partial");
      } else {
        showResult("✗ Incorrect answer", "error");
      }
    } catch (error) {
      console.error("Error checking answer:", error);
      showResult("Error checking answer", "error");
    } finally {
      button.disabled = false;
      button.textContent = "Submit";
    }
  }

  button.addEventListener("click", handleSubmit);
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleSubmit();
  });

  reset.addEventListener("click", () => {
    if (!confirm("Clear all progress?")) return;
    for (const key of Object.keys(solved)) delete solved[key];
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch {
      // nothing was saved in the first place
    }
    renderSolved(puzzles, solved);
    showResult("Cleared.", "warning");
  });
}

// ---------------------------------------------------------------------------
// Hints
// ---------------------------------------------------------------------------

function setupHints(puzzles, hintToggle) {
  const select = document.getElementById("opalHintSelect");
  const button = document.getElementById("opalHintButton");
  const list = document.getElementById("opalHintList");

  const withHints = puzzles.filter((p) => p.hints.length > 0);
  if (withHints.length === 0) {
    hintToggle.hidden = true;
    return;
  }

  // How many hints the visitor has asked for, keyed by hunt and number, so that
  // flipping to another puzzle and back doesn't hide them again.
  const revealed = new Map();
  const byKey = new Map();
  let group = null;
  for (const puzzle of withHints) {
    const key = `${puzzle.hunt}/${puzzle.index}`;
    byKey.set(key, puzzle);
    if (!group || group.label !== puzzle.label) {
      group = document.createElement("optgroup");
      group.label = puzzle.label;
      select.append(group);
    }
    const option = document.createElement("option");
    option.value = key;
    option.textContent = `${puzzle.index}. ${puzzle.title}`;
    group.append(option);
  }

  function render() {
    const puzzle = byKey.get(select.value);
    const shown = revealed.get(select.value) || 0;
    list.replaceChildren();
    for (const hint of puzzle.hints.slice(0, shown)) {
      const li = document.createElement("li");
      appendInline(li, rot13(hint));
      list.append(li);
    }
    button.disabled = shown >= puzzle.hints.length;
    button.textContent = button.disabled
      ? "No more hints"
      : `Show hint ${shown + 1} of ${puzzle.hints.length}`;
  }

  select.addEventListener("change", render);
  button.addEventListener("click", () => {
    revealed.set(select.value, (revealed.get(select.value) || 0) + 1);
    render();
  });
  render();
}

// ---------------------------------------------------------------------------
// Panels
// ---------------------------------------------------------------------------

// The two buttons open one panel at a time; clicking the open one closes it.
function setupPanels() {
  const pairs = [
    ["opalCheckToggle", "opalCheckPanel"],
    ["opalHintToggle", "opalHintPanel"],
  ].map(([toggleId, panelId]) => ({
    toggle: document.getElementById(toggleId),
    panel: document.getElementById(panelId),
  }));

  for (const { toggle, panel } of pairs) {
    toggle.addEventListener("click", () => {
      const opening = panel.hidden;
      for (const other of pairs) {
        other.panel.hidden = true;
        other.toggle.setAttribute("aria-expanded", "false");
      }
      panel.hidden = !opening;
      toggle.setAttribute("aria-expanded", String(opening));
      if (opening) {
        const focusable = panel.querySelector("input, select");
        if (focusable) focusable.focus();
      }
    });
  }
}

function init() {
  const controls = document.querySelector(".opal-controls");
  if (!controls) return;

  const puzzles = loadPuzzles();
  if (puzzles.length === 0) {
    controls.hidden = true;
    return;
  }

  const solved = loadSolved();
  renderSolved(puzzles, solved);
  setupChecker(puzzles, solved);
  setupHints(puzzles, document.getElementById("opalHintToggle"));
  setupPanels();
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
