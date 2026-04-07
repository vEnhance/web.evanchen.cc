# web.evanchen.cc

These are source files for my site
[web.evanchen.cc](https://web.evanchen.cc).

Formerly, the website was generated using [Poole](https://hg.sr.ht/~obensonne/poole).
We now use a custom build script with
[Jinja2](https://jinja.palletsprojects.com/) and
[Python-Markdown](https://python-markdown.github.io/) (with extensions).
The build script is intentionally short, less than 100 lines of code.

## Directory structure

- Content is written in `input/`, and written to `output/`.
  A page `filename.md` is written directly to `output/filename.html`.
  To keep things simple, directory structures are explicitly not supported.
- There is only one Jinja template: `data/page.html.j2`.
- Navigation links on the right are controlled by `data/nav.toml`.
- Python macros are written in `data/macros.py`, available to Jinja.
- The `applets`, `handouts/`, `static/` folders contain additional files
  uploaded directly to the web server from my computer.

## Development

After installing [uv](https://docs.astral.sh/uv/), run

- `uv run prek install` to install pre-commit hooks
- `uv run scripts/build.py` to build
- `uv run scripts/audit.py` to check for broken links
- `uv run scripts/devserver.py` to run a development server
