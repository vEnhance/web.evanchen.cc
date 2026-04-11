document.addEventListener("DOMContentLoaded", () => {
  const url = "https://blog.evanchen.cc/feeds/all.atom.xml";

  fetch(url)
    .then((response) => response.text())
    .then((str) => new DOMParser().parseFromString(str, "application/xml"))
    .then((data) => {
      const entry = data.querySelector("entry");

      const title = entry.querySelector("title").textContent;
      const link = entry.querySelector("link").getAttribute("href");
      const pub_date = entry.querySelector("updated").textContent;

      const cut_title =
        title.length < 45 ? title : title.substring(0, 45) + "…";

      document.getElementById("latest_blog_date").innerHTML =
        pub_date.substring(0, 10);

      const anchor = document.getElementById("latest_blog_anchor");
      anchor.href = link;
      anchor.innerHTML = cut_title;
    })
    .catch((error) => {
      console.error("Failed to fetch blog data:", error);
    });
});
