document.addEventListener("DOMContentLoaded", function () {
  const url = "https://blog.evanchen.cc/feed/";
  fetch("https://api.rss2json.com/v1/api.json?rss_url=" + url)
    .then((response) => response.json())
    .then((data) => {
      const pub_date = data.items[0].pubDate;
      const title = data.items[0].title;
      const link = data.items[0].link;
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
