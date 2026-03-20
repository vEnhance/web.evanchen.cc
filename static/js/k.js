(function () {
  var ks = [];
  document.addEventListener("keydown", function (e) {
    ks.push(e.keyCode);
    if (ks.length > 10) {
      ks.splice(0, ks.length - 10);
    }
    if (ks.length < 10) return;
    if (ks[0] != ks[1]) return;
    if (ks[2] != ks[3]) return;
    if (ks[4] != ks[6]) return;
    if (ks[5] != ks[7]) return;
    const a = ks[9];
    const b = ks[8];
    const d = ks[2];
    const l = ks[4];
    const r = ks[5];
    const u = ks[0];
    if (a * a + b * b * b + d * d * d * d != 2851721) return;
    if (l * l + r * r * r + u * u * u * u != 2145824) return;
    var s =
      String.fromCharCode(a + 7) +
      String.fromCharCode(b + 3) +
      String.fromCharCode(d + 42) +
      String.fromCharCode(l + 42) +
      String.fromCharCode(r + 30) +
      String.fromCharCode(u + 45);
    document.location = "//web.evanchen.cc/" + s.toLowerCase() + ".html";
  });
})();
