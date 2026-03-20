document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".list-chooser a").forEach((link) => {
    link.setAttribute("target", "_blank");
  });
  document.querySelectorAll(".empty-chooser").forEach((chooser) => {
    chooser.innerHTML = "<ul></ul>";
  });
  document.querySelectorAll(".hidden").forEach((el) => {
    const heading = el.getAttribute("data-header");
    const h3 = document.createElement("h3");
    h3.textContent = heading;
    const close = document.createElement("button");
    close.type = "button";
    close.className = "close";
    close.setAttribute("data-dismiss", "alert");
    close.setAttribute("aria-label", "Close");

    const span = document.createElement("span");
    span.setAttribute("aria-hidden", "true");
    span.innerHTML = "&times;";
    close.appendChild(span);

    h3.appendChild(close);
    close.addEventListener("click", () => {
      el.style.display = "none";
    });

    el.prepend(h3);

    const year = el.getAttribute("data-year");
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = "javascript:void(0);";
    a.textContent = year;
    li.appendChild(a);

    let ambient = null;
    let currentElement = el.previousElementSibling;
    while (currentElement) {
      if (currentElement.classList.contains("empty-chooser")) {
        ambient = currentElement.querySelector("ul");
        break;
      }
      currentElement = currentElement.previousElementSibling;
    }
    if (ambient) {
      ambient.appendChild(li);
    }

    li.addEventListener("click", () => {
      document.querySelectorAll(".hidden").forEach((hidden) => {
        hidden.style.display = "none";
      });
      el.style.display = "block";
    });
  });
});
