# web.evanchen.cc

These are source files for my site
[web.evanchen.cc](https://web.evanchen.cc).

Formerly, the website was generated using [Poole](https://hg.sr.ht/~obensonne/poole).
We now use a custom build script with
[Jinja2](https://jinja.palletsprojects.com/) and
[Python-Markdown](https://python-markdown.github.io/) (with extensions).
The [build script](scripts/build.py) is intentionally short, less than 100 lines of code.

## Main content structure

- Content is written in `input/`, and written to `public/`.
  A page `filename.md` is written directly to `public/filename.html`.
  To keep things simple, directory structures are explicitly not supported.
- There is only one Jinja template: `data/page.html.j2`.
- Navigation links on the right are controlled by `data/nav.toml`.
- Python macros are written in `data/macros.py`, available to Jinja.

## Development

After installing [uv](https://docs.astral.sh/uv/), run

- `uv run prek install` to install pre-commit hooks
- `uv run scripts/build.py` to build
- `uv run scripts/audit.py` to check for broken links
- `uv run scripts/devserver.py` to run a development server

## Other directories in the bucket

This website has some subfolders.

### Directories managed with a single authoritative source

- `applets/`: direct copy of `$REPO/applets/`
- `handouts/`: managed using `$REPO/handouts/sync.sh`
- `opals/`: mirrored from an external OPAL repository,
  contains published puzzle PDF files for the
  [OPAL hunt](https://web.evanchen.cc/opal.html)
- `static/`: direct copy of `$REPO/static/`
- `twitch/`: managed using `scripts/upload-twitch-tex-and-pdfs.sh`

### Directories with lots of stuff

(Note to self: periodically check no random files got in here by accident.)

- `exams/`: Contains lots of math contests of various sorts.
  - uploads from `SolArchive` with EGMO, USA(J)MO, USA TST(ST), IMO.
  - ELMO PDF's and award slides
  - OTIS Mock AIME files
  - USEMO problems and reports
  - statistics from some contests
- `notes/`: Manually uploaded lecture notes. Probably pretty fixed now.
- `textbooks/`: Various longer textbooks I've written.
- `upload/`: [The miscellaneous box](https://xkcd.com/1077/).
  Kind of the wild west in here. Read at your own peril.
