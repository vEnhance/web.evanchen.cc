$(document).ready(function () {
  const url = "https://blog.evanchen.cc/feed/";
  $.ajax({
    type: "GET",
    dataType: "jsonp",
    url: "https://api.rss2json.com/v1/api.json?rss_url=" + url,
    success: function (data) {
      const pub_date = data.items[0].pubDate;
      const title = data.items[0].title;
      const link = data.items[0].link;
      const cut_title =
        title.length < 45 ? title : title.substring(0, 45) + "…";
      $("#latest_blog_date").html(pub_date.substring(0, 10));
      $("#latest_blog_anchor").prop("href", link);
      $("#latest_blog_anchor").html(cut_title);
    },
  });
});
