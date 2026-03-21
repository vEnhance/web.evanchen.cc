#!/usr/bin/env python3

import importlib.util
import os
import re
import sys
import tomllib
import urllib.parse
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import markdown
from jinja2 import Environment, FileSystemLoader

PROJECT = Path(__file__).parent.parent
DIR_IN = PROJECT / "input"
DIR_OUT = PROJECT / "output"

MD_EXTENSIONS = ["extra", "smarty", "sane_lists", "mdx_truly_sane_lists"]

RE_EOM = re.compile(r"^---+\s*$", re.MULTILINE)
RE_VARDEF = re.compile(r"^([^\n:=]+?)[:=]((?:.|\n )*)", re.MULTILINE)
RE_MKD = re.compile(r"\.(?:md|mkd|mdown|markdown)$")
RE_REL_URL = re.compile(r'(?<=(?:(?:\n| )src|href)=")([^#/&%].*?)(?=")')

MOUNTPOINTS: list[tuple[str, Path]] = [
    ("/static/", PROJECT / "static"),
    ("/applets/", PROJECT / "data" / "applets"),
    ("/handouts/", PROJECT / "handouts"),
    ("/", DIR_OUT),
]


# =============================================================================
# Build
# =============================================================================


def load_macros() -> dict:
    spec = importlib.util.spec_from_file_location(
        "macros", PROJECT / "data" / "macros.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["macros"] = module
    spec.loader.exec_module(module)
    return {k: v for k, v in module.__dict__.items() if not k.startswith("__")}


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    match = RE_EOM.search(text)
    if match:
        fm_text = text[: match.start()]
        content = text[match.end() :]
    else:
        fm_text = ""
        content = text

    metadata: dict[str, str] = {}
    for m in RE_VARDEF.finditer(fm_text):
        key = m.group(1).strip()
        val = m.group(2).strip()
        val = re.sub(r" *\n +", " ", val)
        metadata[key] = val

    rel = path.relative_to(DIR_IN)
    default_url = RE_MKD.sub(".html", rel.as_posix())
    default_title = path.stem.replace("_", " ")

    return {
        "fname": str(path),
        "url": default_url,
        "title": default_title,
        **metadata,
        "_content": content,
    }


def load_nav_links() -> list[dict]:
    with open(PROJECT / "data" / "nav_links.toml", "rb") as f:
        data = tomllib.load(f)
    return [{"_nav_only": True, **link} for link in data.get("links", [])]


def build() -> None:
    os.chdir(PROJECT)

    DIR_OUT.mkdir(exist_ok=True)
    macros = load_macros()

    pages = [parse_page(p) for p in sorted(DIR_IN.rglob("*.md"))]
    pages += load_nav_links()
    pages.sort(key=lambda p: int(p.get("menu-position", 9999)))

    md_env = Environment(autoescape=False, keep_trailing_newline=True)
    md_env.globals.update(macros)
    md_env.globals["pages"] = pages

    tmpl_env = Environment(
        loader=FileSystemLoader(str(PROJECT / "data")),
        autoescape=False,
        keep_trailing_newline=True,
    )
    tmpl_env.globals.update(macros)
    tmpl_env.globals["pages"] = pages

    template = tmpl_env.get_template("page.html")
    md_converter = markdown.Markdown(extensions=MD_EXTENSIONS)

    for page in pages:
        if page.get("_nav_only"):
            continue

        print(f"* {page['url']}")

        md_env.globals["page"] = page
        rendered_md = md_env.from_string(page["_content"]).render()

        md_converter.reset()
        content_html = md_converter.convert(rendered_md)

        html = template.render(page=page, pages=pages, content=content_html)
        html = RE_REL_URL.sub(lambda m: urllib.parse.urljoin("/", m.group(1)), html)

        src_rel = Path(page["fname"]).relative_to(DIR_IN)
        out_path = DIR_OUT / src_rel.with_suffix(".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")


# =============================================================================
# Audit: HTML validation + broken links
# =============================================================================


class _HTMLAuditor(HTMLParser):
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


def _validate_html(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8")
    errors = []

    if not html.lstrip().startswith("<!DOCTYPE html>"):
        errors.append("missing or malformed <!DOCTYPE html>")

    auditor = _HTMLAuditor()
    auditor.feed(html)
    errors.extend(auditor.errors)
    return errors


class _LinkExtractor(HTMLParser):
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


def _resolve_url(url_path: str, skip_prefixes: tuple) -> Path | None:
    if any(url_path.startswith(p) for p in skip_prefixes):
        return None
    for prefix, directory in MOUNTPOINTS:
        if url_path.startswith(prefix):
            fspath = directory / url_path[len(prefix) :]
            if fspath.is_dir():
                fspath = fspath / "index.html"
            return fspath
    return None


def _broken_links(path: Path, skip_prefixes: tuple) -> list[str]:
    extractor = _LinkExtractor()
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
        fspath = _resolve_url(abs_path, skip_prefixes)
        if fspath is not None and not fspath.exists():
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
        results[path.name].extend(f"html: {e}" for e in _validate_html(path))
        results[path.name].extend(
            f"broken link: {url}" for url in _broken_links(path, skip_prefixes)
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
    build()
    if not audit():
        sys.exit(1)
