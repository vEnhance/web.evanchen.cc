#!/usr/bin/env python3

import importlib.util
import json
import os
import re
import sys
import tomllib
import urllib.parse
import urllib.request
from pathlib import Path

import frontmatter
from jinja2 import Environment, FileSystemLoader
from markdown_it_pyrs import MarkdownIt

REPO_ROOT = Path(__file__).parent.parent
MACROS_PATH = REPO_ROOT / "data" / "macros.py"
DIR_IN = REPO_ROOT / "input"
DIR_OUT = REPO_ROOT / "output"
INSTAGRAM_LIST = REPO_ROOT / "data" / "instagram.txt"
INSTAGRAM_COUNT = 8  # keep in sync with scripts/instagram.py
LATEST_BLOG_URL = "https://blog.evanchen.cc/latest.json"
LATEST_BLOG_TIMEOUT = 5  # seconds
LATEST_BLOG_TITLE_LENGTH = 45  # keep in sync with static/js/blog.js
MARKDOWN_EXTENSIONS = ["table", "footnote", "smartquotes", "deflist", "strikethrough"]

RE_REL_URL = re.compile(r'(?<=(?:(?:\n| )src|href)=")([^#/&%].*?)(?=")')


def load_macros() -> dict:
    spec = importlib.util.spec_from_file_location("macros", MACROS_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["macros"] = module
    spec.loader.exec_module(module)
    return {k: v for k, v in module.__dict__.items() if not k.startswith("__")}


def get_nav_data(toml_path: Path) -> list[dict]:
    with open(toml_path, "rb") as f:
        data = tomllib.load(f)
    out = []
    for block_dict in data["block"]:
        subpages = block_dict.pop("subpages")
        out.append(block_dict)
        for sub_dict in subpages:
            sub_dict["indent"] = True
            out.append(sub_dict)
    return out


def get_instagram_ids(path: Path) -> list[str]:
    """Most recent posts, newest first (the file is oldest first)."""
    lines = (line.strip() for line in path.read_text().splitlines())
    ids = [line for line in lines if line and not line.startswith("#")]
    return ids[::-1][:INSTAGRAM_COUNT]


def get_latest_blog() -> dict | None:
    """Latest blog post as a no-JS fallback; blog.js refreshes it client-side."""
    try:
        # Cloudflare rejects the default Python-urllib User-Agent
        req = urllib.request.Request(
            LATEST_BLOG_URL, headers={"User-Agent": "web.evanchen.cc-build"}
        )
        with urllib.request.urlopen(req, timeout=LATEST_BLOG_TIMEOUT) as r:
            data = json.load(r)
        title, url, date = data["title"], data["url"], data["date"]
    except (OSError, ValueError, KeyError, TypeError) as e:  # never break the build
        print(f"! Could not fetch latest blog post: {e!r}", file=sys.stderr)
        return None
    if len(title) >= LATEST_BLOG_TITLE_LENGTH:
        title = title[:LATEST_BLOG_TITLE_LENGTH] + "…"
    return {"title": title, "url": url, "date": date[:10]}


def build() -> None:
    os.chdir(REPO_ROOT)
    DIR_OUT.mkdir(exist_ok=True)
    macros = load_macros()
    md_env = Environment(autoescape=False, keep_trailing_newline=True)
    md_env.globals.update(macros)
    tmpl_env = Environment(
        loader=FileSystemLoader(str(REPO_ROOT / "data")),
        autoescape=False,
        keep_trailing_newline=True,
    )
    tmpl_env.globals["nav_links"] = get_nav_data(REPO_ROOT / "data" / "nav.toml")
    tmpl_env.globals["instagram_ids"] = get_instagram_ids(INSTAGRAM_LIST)
    tmpl_env.globals["latest_blog"] = get_latest_blog()
    tmpl_env.globals.update(macros)
    template = tmpl_env.get_template("page.html.j2")
    md_converter = MarkdownIt().enable_many(MARKDOWN_EXTENSIONS)

    for path in DIR_IN.rglob("*.md"):
        print(f"* {path}")
        src = path.stem
        with open(path) as f:
            page = frontmatter.load(f)
        md_env.globals["page"] = page
        rendered_md = md_env.from_string(page.content).render()

        content_html = md_converter.render(rendered_md)
        html = template.render(page=page, src=src, content=content_html)
        html = RE_REL_URL.sub(lambda m: urllib.parse.urljoin("/", m.group(1)), html)

        out_path = DIR_OUT / f"{src}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    build()
