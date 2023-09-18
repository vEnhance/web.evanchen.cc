$(document).ready(function () {
  $(".trick-container").css("font-family", "Verdana, Geneva, sans-serif");
  $(".trick-container").css("font-size", "18px");
  $(".rank-select").select2({ width: "5em" });
  $(".suit-select").select2({ width: "8em" });
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
  var done = false;

  function getInputs() {
    const r0 = ranks.indexOf($("#rank-0").val()) - 1;
    const r1 = ranks.indexOf($("#rank-1").val()) - 1;
    const r2 = ranks.indexOf($("#rank-2").val()) - 1;
    const r3 = ranks.indexOf($("#rank-3").val()) - 1;
    const s0 = suits.indexOf($("#suit-0").val()) - 1;
    const s1 = suits.indexOf($("#suit-1").val()) - 1;
    const s2 = suits.indexOf($("#suit-2").val()) - 1;
    const s3 = suits.indexOf($("#suit-3").val()) - 1;
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
    if (state) {
      $("#trick-button").attr("disabled", false);
      $("#trick-button").removeClass("btn-danger");
      $("#trick-button").addClass("btn-primary");
      $("#trick-button").html("Do magic");
    } else {
      $("#trick-button").attr("disabled", true);
      $("#trick-button").removeClass("btn-primary");
      $("#trick-button").addClass("btn-danger");
      $("#trick-button").html("Not ready yet");
    }
  }

  $(".form-select").on("change", function () {
    if (!done) {
      const data = getInputs();
      buttonSetState(isValid(data));
    }
  });

  $("#trick-button").on("click", function () {
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
    $("#answer").html("Last card: " + ranks[r + 1] + " " + suits[s + 1]);
    done = true;
    $("#trick-button").attr("disabled", true);
    $("#trick-button").removeClass("btn-primary");
    $("#trick-button").addClass("btn-success");
    $("#trick-button").html("Done!");
  });

  buttonSetState(false);
});
