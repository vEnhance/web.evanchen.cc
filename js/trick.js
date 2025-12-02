document.addEventListener("DOMContentLoaded", function () {
  const trickContainers = document.querySelectorAll(".trick-container");
  trickContainers.forEach((container) => {
    container.style.fontFamily = "Verdana, Geneva, sans-serif";
    container.style.fontSize = "18px";
  });

  // Initialize Slim Select for all rank and suit selects
  const rankSelects = [];
  const suitSelects = [];
  for (let i = 0; i < 4; i++) {
    rankSelects.push(
      new SlimSelect({
        select: `#rank-${i}`,
      })
    );
    suitSelects.push(
      new SlimSelect({
        select: `#suit-${i}`,
      })
    );
  }

  const ranks = [
    "...",
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
  ];
  const suits = ["...", "♣Clubs", "♦Diamonds", "♥Hearts", "♠Spades"];
  let done = false;

  function getInputs() {
    const r0 = ranks.indexOf(document.getElementById("rank-0").value) - 1;
    const r1 = ranks.indexOf(document.getElementById("rank-1").value) - 1;
    const r2 = ranks.indexOf(document.getElementById("rank-2").value) - 1;
    const r3 = ranks.indexOf(document.getElementById("rank-3").value) - 1;
    const s0 = suits.indexOf(document.getElementById("suit-0").value) - 1;
    const s1 = suits.indexOf(document.getElementById("suit-1").value) - 1;
    const s2 = suits.indexOf(document.getElementById("suit-2").value) - 1;
    const s3 = suits.indexOf(document.getElementById("suit-3").value) - 1;
    const data = [r0, r1, r2, r3, s0, s1, s2, s3];
    if (data.includes(-1)) return null;
    return data;
  }

  function isValid(data) {
    if (data === null) {
      return false;
    }
    for (let i = 0; i < 4; ++i) {
      for (let j = i + 1; j < 4; ++j) {
        if (data[i] == data[j] && data[i + 4] == data[j + 4]) {
          return false;
        }
      }
    }
    return true;
  }

  function buttonSetState(state) {
    if (done) {
      return;
    }
    const button = document.getElementById("trick-button");
    if (state) {
      button.disabled = false;
      button.classList.remove("btn-danger");
      button.classList.add("btn-primary");
      button.innerHTML = "Do magic";
    } else {
      button.disabled = true;
      button.classList.remove("btn-primary");
      button.classList.add("btn-danger");
      button.innerHTML = "Not ready yet";
    }
  }

  const formSelects = document.querySelectorAll(".form-select");
  formSelects.forEach((select) => {
    select.addEventListener("change", function () {
      if (!done) {
        const data = getInputs();
        buttonSetState(isValid(data));
      }
    });
  });

  document.getElementById("trick-button").addEventListener("click", function () {
    const data = getInputs();
    if (!isValid(data)) {
      return;
    }
    const [r0, r1, r2, r3, s0, s1, s2, s3] = data;
    const s = s0;
    const [a, b, c] = [100 * r1 + s1, 100 * r2 + s2, 100 * r3 + s3];
    let r = r0;
    if (a < b && a < c) {
      r += b < c ? 1 : 2;
    } else if (a > b && a > c) {
      r += b < c ? 5 : 6;
    } else {
      r += b < c ? 3 : 4;
    }
    r %= 13;
    document.getElementById("answer").innerHTML =
      "Last card: " + ranks[r + 1] + " " + suits[s + 1];
    done = true;
    const button = document.getElementById("trick-button");
    button.disabled = true;
    button.classList.remove("btn-primary");
    button.classList.add("btn-success");
    button.innerHTML = "Done!";
  });

  buttonSetState(false);
});
