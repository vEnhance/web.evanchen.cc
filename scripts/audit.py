#!/usr/bin/env python3

import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import ClassVar
from urllib.parse import urljoin, urlparse

PROJECT = Path(__file__).parent.parent
DIR_OUT = PROJECT / "output"

MOUNTPOINTS: list[tuple[str, Path]] = [
    ("/static/", PROJECT / "static"),
    ("/applets/", PROJECT / "applets"),
    ("/handouts/", PROJECT / "handouts"),
    ("/", DIR_OUT),
]

# =============================================================================
# Audit: HTML validation + broken links
# =============================================================================


class HTMLAuditor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.errors: list[str] = []
        self._ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        seen: set[str] = set()
        attr_dict: dict[str, str | None] = {}
        for name, value in attrs:
            if name in seen:
                self.errors.append(f"duplicate attribute '{name}' on <{tag}>")
            seen.add(name)
            attr_dict[name] = value

        id_val = attr_dict.get("id")
        if id_val is not None:
            if id_val in self._ids:
                self.errors.append(f"duplicate id='{id_val}'")
            self._ids.add(id_val)

        if tag == "img" and not attr_dict.get("alt"):
            self.errors.append(f"<img> missing alt (src={attr_dict.get('src', '?')})")

        for attr in ("src", "href"):
            if attr in attr_dict and attr_dict[attr] == "":
                self.errors.append(f"empty {attr} on <{tag}>")


def validate_html(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    errors = []

    if not html.lstrip().startswith("<!DOCTYPE html>"):
        errors.append("missing or malformed <!DOCTYPE html>")

    auditor = HTMLAuditor()
    auditor.feed(html)
    errors.extend(auditor.errors)
    return errors


class LinkExtractor(HTMLParser):
    ATTRS: ClassVar[dict[str, str]] = {
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
        attr = self.ATTRS.get(tag)
        if attr:
            for name, value in attrs:
                if name == attr and value:
                    self.links.append(value)


def resolve_url(url_path: str, skip_prefixes: tuple) -> Path | None:
    if any(url_path.startswith(p) for p in skip_prefixes):
        return None
    for prefix, directory in MOUNTPOINTS:
        if url_path.startswith(prefix):
            fspath = directory / url_path[len(prefix) :]
            if fspath.is_dir():
                fspath = fspath / "index.html"
            return fspath
    return None


def asset_exists(fspath: Path) -> bool:
    if fspath.exists():
        return True
    # Handout PDFs are LaTeX build artifacts, absent from a fresh checkout;
    # check the source instead.
    return (
        fspath.suffix == ".pdf"
        and fspath.is_relative_to(PROJECT / "handouts")
        and fspath.with_suffix(".tex").exists()
    )


def broken_links(path: Path, skip_prefixes: tuple) -> list[str]:
    extractor = LinkExtractor()
    extractor.feed(path.read_text(encoding="utf-8"))
    bad = []
    base = f"/{path.name}"
    for raw in extractor.links:
        p = urlparse(raw)
        if p.scheme in ("http", "https", "mailto", "data", "javascript"):
            continue
        if raw.startswith("//"):
            continue
        if not p.path:
            continue
        abs_path = urlparse(urljoin(base, raw)).path
        fspath = resolve_url(abs_path, skip_prefixes)
        if fspath is not None and not asset_exists(fspath):
            bad.append(raw)
    return bad


def audit() -> bool:
    skip_prefixes = tuple(
        line.strip()
        for line in (PROJECT / "data" / "EXTDIRS").read_text().splitlines()
        if line.strip()
    )

    results: dict[str, list[str]] = defaultdict(list)
    for path in sorted(DIR_OUT.glob("*.html")):
        results[path.name].extend(f"html: {e}" for e in validate_html(path))
        results[path.name].extend(
            f"broken link: {url}" for url in broken_links(path, skip_prefixes)
        )

    errors = {k: v for k, v in results.items() if v}
    if not errors:
        return True

    for page, messages in sorted(errors.items()):
        print(f"\n{page}", file=sys.stderr)
        for msg in messages:
            print(f"  {msg}", file=sys.stderr)
    total = sum(len(v) for v in errors.values())
    print(f"\n{total} error(s) in {len(errors)} file(s).", file=sys.stderr)
    return False


if __name__ == "__main__":
    if audit():
        print("👌 seems to work")
    else:
        print("❌ ばか")
        sys.exit(1)
