#!/usr/bin/env python3

import importlib.util
import os
import re
import sys
import tomllib
import urllib.parse
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

PROJECT = Path(__file__).parent
DIR_IN = PROJECT / "input"
DIR_OUT = PROJECT / "output"

MD_EXTENSIONS = ["extra", "smarty", "sane_lists", "mdx_truly_sane_lists"]

RE_EOM = re.compile(r"^---+\s*$", re.MULTILINE)
RE_VARDEF = re.compile(r"^([^\n:=]+?)[:=]((?:.|\n )*)", re.MULTILINE)
RE_MKD = re.compile(r"\.(?:md|mkd|mdown|markdown)$")
RE_REL_URL = re.compile(r'(?<=(?:(?:\n| )src|href)=")([^#/&%].*?)(?=")')


def load_macros() -> dict:
    spec = importlib.util.spec_from_file_location("macros", PROJECT / "macros.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["macros"] = module
    spec.loader.exec_module(module)
    return {k: v for k, v in module.__dict__.items() if not k.startswith("__")}


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    # Split at first --- line into front matter and content
    match = RE_EOM.search(text)
    if match:
        fm_text = text[: match.start()]
        content = text[match.end() :]
    else:
        fm_text = ""
        content = text

    # Parse key: value (or key = value) pairs from front matter
    metadata: dict[str, str] = {}
    for m in RE_VARDEF.finditer(fm_text):
        key = m.group(1).strip()
        val = m.group(2).strip()
        val = re.sub(r" *\n +", " ", val)  # collapse line continuations
        metadata[key] = val

    # Default url and title derived from filename; front matter can override
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
    """Load nav-only entries (external links, PDFs) from nav_links.toml."""
    with open(PROJECT / "nav_links.toml", "rb") as f:
        data = tomllib.load(f)
    return [{"_nav_only": True, **link} for link in data.get("links", [])]


def build() -> None:
    os.chdir(PROJECT)
    DIR_OUT.mkdir(exist_ok=True)
    macros = load_macros()

    pages = [parse_page(p) for p in sorted(DIR_IN.rglob("*.md"))]
    pages += load_nav_links()
    pages.sort(key=lambda p: int(p.get("menu-position", 9999)))

    # Jinja2 environment for pre-processing markdown content
    # autoescape=False because macros return raw HTML intentionally
    md_env = Environment(autoescape=False, keep_trailing_newline=True)
    md_env.globals.update(macros)
    md_env.globals["pages"] = pages

    # Jinja2 environment for rendering page.html
    tmpl_env = Environment(
        loader=FileSystemLoader(str(PROJECT)),
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

        # Step 1: pre-process markdown source through Jinja2
        # (evaluates {{ macro_call() }} expressions in .md files)
        md_env.globals["page"] = page
        rendered_md = md_env.from_string(page["_content"]).render()

        # Step 2: convert markdown to HTML
        md_converter.reset()
        content_html = md_converter.convert(rendered_md)

        # Step 3: render the full page via page.html template
        html = template.render(page=page, pages=pages, content=content_html)

        # Step 4: rewrite relative href/src values to absolute paths
        html = RE_REL_URL.sub(lambda m: urllib.parse.urljoin("/", m.group(1)), html)

        src_rel = Path(page["fname"]).relative_to(DIR_IN)
        out_path = DIR_OUT / src_rel.with_suffix(".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build()
