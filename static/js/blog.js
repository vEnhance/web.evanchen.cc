document.addEventListener("DOMContentLoaded", () => {
  const url = "https://blog.evanchen.cc/latest.json";

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const title = data.title;
      const link = data.url;
      const pub_date = data.date;

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
