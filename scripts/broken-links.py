#!/usr/bin/env python3
"""Check for broken local links across all compiled HTML pages.

Parses every file in output/*.html, resolves each href/src against
the same virtual filesystem layout as serve.py, and reports targets
that don't exist on disk. External URLs (http/https) are skipped.
"""

import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

REPO = Path(__file__).resolve().parent.parent

MOUNTPOINTS: list[tuple[str, Path]] = [
    ("/static/", REPO / "static"),
    ("/applets/", REPO / "applets"),
    ("/handouts/", REPO / "handouts"),
    ("/", REPO / "output"),
]
SKIP_PREFIXES = tuple(
    line.strip() for line in (REPO / "EXTDIRS").read_text().splitlines() if line.strip()
)


def resolve(url_path: str) -> Path | None:
    """Map a root-relative URL path to a filesystem path.
    Returns None if the path is in a redirected/skipped prefix."""
    if any(url_path.startswith(p) for p in SKIP_PREFIXES):
        return None
    for prefix, directory in MOUNTPOINTS:
        if url_path.startswith(prefix):
            fspath = directory / url_path[len(prefix) :]
            # Treat bare directories as index.html
            if fspath.is_dir():
                fspath = fspath / "index.html"
            return fspath
    return None


class LinkExtractor(HTMLParser):
    _ATTRS: dict[str, str] = {
        "a": "href",
        "img": "src",
        "link": "href",
        "script": "src",
        "source": "src",
    }

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = self._ATTRS.get(tag)
        if attr:
            for name, value in attrs:
                if name == attr and value:
                    self.links.append(value)


def broken_links(html_file: Path) -> list[str]:
    extractor = LinkExtractor()
    extractor.feed(html_file.read_text(encoding="utf-8"))
    bad = []
    base = f"/{html_file.name}"
    for raw in extractor.links:
        p = urlparse(raw)
        if p.scheme in ("http", "https", "mailto", "data", "javascript"):
            continue
        if raw.startswith("//"):  # protocol-relative external URL
            continue
        if not p.path:  # fragment-only
            continue
        abs_path = urlparse(urljoin(base, raw)).path
        fspath = resolve(abs_path)
        if fspath is not None and not fspath.exists():
            bad.append(raw)
    return bad


def main() -> int:
    html_files = sorted((REPO / "output").glob("*.html"))
    results: dict[str, list[str]] = defaultdict(list)

    for f in html_files:
        bad = broken_links(f)
        if bad:
            results[f.name] = bad

    if not results:
        print("No broken links found.")
        return 0

    total = 0
    for page, links in sorted(results.items()):
        print(f"\n{page}")
        for url in links:
            print(f"  {url}")
            total += 1
    print(f"\n{total} broken link(s) in {len(results)} file(s).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
