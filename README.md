# web.evanchen.cc

These are source files for my site
[web.evanchen.cc](https://web.evanchen.cc).

Formerly, the website was generated using [Poole](https://hg.sr.ht/~obensonne/poole).
We now use a custom build script with
[Jinja2](https://jinja.palletsprojects.com/) and
[Python-Markdown](https://python-markdown.github.io/).

## Development

After installing [uv](https://docs.astral.sh/uv/), run

- `uv run scripts/build.py` to build
- `uv run scripts/devserver.py` to run a development server
