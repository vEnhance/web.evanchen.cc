// Answer checker with salt support
// This file works with answer_hashes.js to validate user answers

const SALT = "opal_puzzle_hunt_secret_salt";

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

async function checkAnswer(userInput) {
  // Normalize user input
  const normalized = normalizeAnswer(userInput);

  // Hash the normalized input
  const hashedInput = await hashAnswer(normalized);

  // Check if hash exists in the answer list
  return ANSWER_HASHES.includes(hashedInput);
}

// DOM utility functions for easy integration
function setupAnswerChecker(inputSelector, buttonSelector, resultSelector) {
  const input = document.querySelector(inputSelector);
  const button = document.querySelector(buttonSelector);
  const result = document.querySelector(resultSelector);

  if (!input || !button || !result) {
    console.error("Answer checker setup failed: missing DOM elements");
    return;
  }

  async function handleSubmit() {
    const userAnswer = input.value.trim();

    if (!userAnswer) {
      result.textContent = "Please enter an answer";
      result.className = "result warning";
      return;
    }

    button.disabled = true;
    button.textContent = "Checking...";

    try {
      const isCorrect = await checkAnswer(userAnswer);

      if (isCorrect) {
        result.textContent = "✓ Correct!";
        result.className = "result success";
        input.value = "";
      } else {
        result.textContent = "✗ Incorrect answer";
        result.className = "result error";
      }
    } catch (error) {
      console.error("Error checking answer:", error);
      result.textContent = "Error checking answer";
      result.className = "result error";
    } finally {
      button.disabled = false;
      button.textContent = "Submit";
    }
  }

  // Handle button click
  button.addEventListener("click", handleSubmit);

  // Handle Enter key in input
  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      handleSubmit();
    }
  });
}

// Initialize the answer checker when the page loads
document.addEventListener("DOMContentLoaded", function () {
  // Check if ANSWER_HASHES is loaded
  if (typeof ANSWER_HASHES === "undefined") {
    document.getElementById("result").textContent =
      "Error: Answer hashes not loaded. Run generate_hashes.py first!";
    document.getElementById("result").className = "result error";
    document.getElementById("result").style.display = "block";
    document.getElementById("submitButton").disabled = true;
    return;
  }

  // Set up the answer checker
  setupAnswerChecker("#answerInput", "#submitButton", "#result");

  // Show result div when there's content
  const resultDiv = document.getElementById("result");
  const observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      if (mutation.type === "childList" || mutation.type === "characterData") {
        if (resultDiv.textContent.trim()) {
          resultDiv.style.display = "block";
        }
      }
    });
  });
  observer.observe(resultDiv, {
    childList: true,
    subtree: true,
    characterData: true,
  });
});
