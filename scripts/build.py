#!/usr/bin/env python3

import importlib.util
import os
import re
import sys
import tomllib
import urllib.parse
from pathlib import Path

import frontmatter
from jinja2 import Environment, FileSystemLoader
from markdown_it_pyrs import MarkdownIt

REPO_ROOT = Path(__file__).parent.parent
MACROS_PATH = REPO_ROOT / "data" / "macros.py"
DIR_IN = REPO_ROOT / "input"
DIR_OUT = REPO_ROOT / "output"
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
