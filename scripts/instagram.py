#!/usr/bin/env python3
"""Manage the Instagram banner shown at the top of every page.

  instagram.py               look up new posts, append them, make missing thumbnails
  instagram.py URL [IMAGE]   add one post by hand (if the lookup fails)
  instagram.py --force       also remake thumbnails that already exist

New posts are found via the LightWidget widget page (which visitors
never load), falling back to Instagram's unofficial web profile endpoint.

Thumbnails are written to instagram/<id>.webp (git-ignored) using ImageMagick;
upload them with scripts/sync.sh. If downloading from Instagram fails,
pass a local IMAGE file instead.
"""

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIST_PATH = REPO / "data" / "instagram.txt"
IMG_DIR = REPO / "instagram"
BANNER_COUNT = 8  # keep in sync with scripts/build.py
THUMB_SIZE = 192  # px; banner tiles are ~90 CSS px wide, so 2x for hi-dpi
USER_AGENT = "Mozilla/5.0 (compatible; web.evanchen.cc banner script)"
USERNAME = "evanchen.cc"
PROFILE_API = (
    f"https://i.instagram.com/api/v1/users/web_profile_info/?username={USERNAME}"
)
IG_APP_ID = "936619743392459"  # public app ID used by instagram.com itself
LIGHTWIDGET = (
    "https://cdn.lightwidget.com/widgets/90dc888fdd63572186f83253c9a50415.html"
)
SHORTCODE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

RE_ID = re.compile(r"^[A-Za-z0-9_-]+$")
RE_URL = re.compile(r"instagram\.com/(?:[^/]+/)?(?:p|reel|tv)/([A-Za-z0-9_-]+)")
RE_LIGHTWIDGET_POST = re.compile(
    r'href="https://www\.instagram\.com/p/([A-Za-z0-9_-]+)/".*?data-src="([^"]+)"',
    re.DOTALL,
)
RE_OG_IMAGE = re.compile(
    r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"'
    r'|<meta[^>]+content="([^"]+)"[^>]+property="og:image"'
)


def parse_id(s: str) -> str:
    if m := RE_URL.search(s):
        return m.group(1)
    if RE_ID.match(s):
        return s
    sys.exit(f"Can't find an Instagram post ID in {s!r}")


def media_id(shortcode: str) -> int:
    """Decode a post ID to Instagram's numeric media ID, which increases with time."""
    n = 0
    for c in shortcode:
        n = n * 64 + SHORTCODE_ALPHABET.index(c)
    return n


def read_ids() -> list[str]:
    """Post IDs, oldest first."""
    lines = (line.strip() for line in LIST_PATH.read_text().splitlines())
    return [line for line in lines if line and not line.startswith("#")]


def fetch(url: str, headers: dict[str, str] | None = None) -> bytes:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, **(headers or {})}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def recent_from_profile() -> dict[str, str | None]:
    """Recent posts as {id: full image URL}, from Instagram's web profile endpoint."""
    data = json.loads(fetch(PROFILE_API, {"X-IG-App-ID": IG_APP_ID}))
    edges = data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]
    return {e["node"]["shortcode"]: e["node"].get("display_url") for e in edges}


def recent_from_lightwidget() -> dict[str, str | None]:
    """Recent posts as {id: full image URL}, scraped from the LightWidget page."""
    page = fetch(LIGHTWIDGET).decode("utf-8", "replace")
    return {i: html.unescape(url) for i, url in RE_LIGHTWIDGET_POST.findall(page)}


def discover() -> dict[str, str | None] | None:
    for name, source in [
        ("LightWidget", recent_from_lightwidget),
        ("Instagram", recent_from_profile),
    ]:
        print(f"Looking up recent posts via {name}...")
        try:
            posts = source()
        except Exception as e:  # noqa: BLE001
            print(f"  FAILED: {e}", file=sys.stderr)
            continue
        if posts:
            return posts
        print("  FAILED: no posts found", file=sys.stderr)
    return None


def download_og_image(post_id: str) -> bytes:
    """Last resort: the post page's preview image, which is cropped tighter."""
    page = fetch(f"https://www.instagram.com/p/{post_id}/").decode("utf-8", "replace")
    m = RE_OG_IMAGE.search(page)
    if m is None:
        raise RuntimeError("no og:image tag on the post page (login wall?)")
    return fetch(html.unescape(m.group(1) or m.group(2)))


def make_thumb(data: bytes, out: Path) -> None:
    """Center-crop to a square THUMB_SIZE WebP."""
    out.parent.mkdir(exist_ok=True)
    size = f"{THUMB_SIZE}x{THUMB_SIZE}"
    subprocess.run(
        ["magick", "-", "-auto-orient", "-resize", f"{size}^", "-gravity", "center",
         "-extent", size, "-strip", "-quality", "80", f"webp:{out}"],
        input=data,
        check=True,
    )  # fmt: skip
    print(f"  wrote {out.relative_to(REPO)} ({out.stat().st_size // 1024} KB)")


def ensure_thumb(
    post_id: str,
    image: Path | None = None,
    image_url: str | None = None,
    force: bool = False,
) -> bool:
    out = IMG_DIR / f"{post_id}.webp"
    if image is not None:
        make_thumb(image.read_bytes(), out)
        return True
    if out.exists() and not force:
        return True
    try:
        if image_url:
            print(f"* {post_id}: downloading")
            data = fetch(image_url)
        else:
            print(f"* {post_id}: downloading preview image (tighter crop)")
            data = download_og_image(post_id)
        make_thumb(data, out)
    except Exception as e:  # noqa: BLE001
        print(f"  FAILED: {e}", file=sys.stderr)
        print(
            f"  Save the image manually and run: instagram.py {post_id} FILE",
            file=sys.stderr,
        )
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("url", nargs="?", help="post URL or ID")
    parser.add_argument("image", nargs="?", type=Path, help="local image file")
    parser.add_argument(
        "-f", "--force", action="store_true", help="remake existing thumbnails"
    )
    args = parser.parse_args()

    ids = read_ids()
    posts = discover() if args.image is None else {}
    if posts is None:
        print("Couldn't look up recent posts.", file=sys.stderr)
        posts = {}
    if args.url is None:
        # only posts newer than the newest one we have, so pinned or
        # deliberately removed posts don't get re-added
        newest = max((media_id(i) for i in ids), default=-1)
        new = sorted((i for i in posts if media_id(i) > newest), key=media_id)
        if new:
            with LIST_PATH.open("a") as f:
                f.writelines(i + "\n" for i in new)
            ids += new
            print(f"Added {len(new)} new post(s): {' '.join(new)}")
        else:
            print("No new posts.")
        results = [
            ensure_thumb(i, image_url=posts.get(i), force=args.force)
            for i in ids[-BANNER_COUNT:]
        ]
        ok = all(results) and bool(posts)
    else:
        post_id = parse_id(args.url)
        if post_id in ids:
            print(f"{post_id} is already in {LIST_PATH.relative_to(REPO)}")
        else:
            with LIST_PATH.open("a") as f:
                f.write(post_id + "\n")
            print(f"Added {post_id} to {LIST_PATH.relative_to(REPO)}")
        ok = ensure_thumb(post_id, args.image, posts.get(post_id), args.force)
    if ok:
        print("Done. Upload with scripts/sync.sh before pushing.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
