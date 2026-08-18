import csv
import datetime
import functools
import json
import tomllib
from html import escape
from pathlib import Path

from git.repo import Repo
from jinja2 import Environment, FileSystemLoader
from markdown_it_pyrs import MarkdownIt

_md = MarkdownIt()

DATA_DIR = Path(__file__).parent
OPAL_JSON_PATH = DATA_DIR / "opal.json"

# Reusable chunks of HTML that macros render; unlike the pages themselves these
# are already HTML, so they get autoescaping.
_component_env = Environment(
    loader=FileSystemLoader(str(DATA_DIR / "components")),
    autoescape=True,
    trim_blocks=True,
    lstrip_blocks=True,
)

repo = Repo(Path(__file__).parent, search_parent_directories=True)
tree = repo.head.commit.tree

GITHUB_BASE = "https://github.com/vEnhance/web.evanchen.cc"


def handout_link_src(name: str, filename=None) -> str:
    filename = filename or name
    return (
        f'<a href="handouts/{name}/{filename}.pdf">(pdf)</a>'
        " "
        f'<a href="{GITHUB_BASE}/tree/main/handouts/{name}">(git)</a>'
        "<br>"
    )


def page_footer(src: str) -> str:
    input_path = Path("input") / f"{src}.md"
    try:
        blob = tree[str(input_path)]
    except KeyError:
        return (
            '<div class="text-muted">\n'
            f'View the <a href="{GITHUB_BASE}">source repository</a>.\n'
            "</div>\n"
            '<div class="font-italic text-muted">\n'
            "This hidden page not under public version control.\n"
            "</div>"
        )
    else:
        commit = next(repo.iter_commits(paths=blob.path, max_count=1))
        last_update_dt = datetime.datetime.fromtimestamp(
            commit.committed_date, tz=datetime.UTC
        )
        last_update_str = last_update_dt.strftime("%a %-d %b %Y, %H:%M:%S UTC")
        return (
            "<div>\n"
            f'<a href="{GITHUB_BASE}">Source repository (git)</a> &bullet;\n'
            f'<a href="{GITHUB_BASE}/commits/main/{input_path}">Revision history</a> &bullet;\n'
            f'<a href="{GITHUB_BASE}/edit/main/{input_path}">Suggest edit</a>\n'
            "</div>\n"
            f'<div class="text-muted">Updated {last_update_str} by\n'
            f'<a href="{GITHUB_BASE}/commit/{commit.hexsha}"><code>{commit.hexsha[0:12]}</code></a>\n'
            "</div>"
        )


def get_twitch_table() -> str:
    if (data_directory := Path("data/twitch/")).exists():
        csv_path = data_directory / "problems.csv"
        url_path = data_directory / "urls.lock"
    else:
        return "(Error: could not read Twitch table)"

    with open(url_path, "rb") as f:
        url_dict = tomllib.load(f)

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)

    data.sort(key=lambda row: (-int(row["N"]), row["Source"]))

    out = ""
    out += r'<table cellpadding="5">' + "\n"
    out += (
        r"<tr><th>Episode</th><th>Problem</th><th>PDF</th><th>Src</th><th>YouTube</th></tr>"
        + "\n"
    )

    for row in data:
        n = row["N"]
        key: str = row["Source"]
        youtube_url = row["YouTube"]

        if key.startswith("!"):  # coding problem
            pdf_url = None
            src_type = "git"
            if key.startswith("!AtCoder"):
                pid = key[8:].strip().replace(" ", "")
                contest = pid[:-1].lower()
                src_url = f"https://github.com/vEnhance/evan-learns-ioi/tree/main/AtCoder/{pid}"
                url = f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{pid[-1].lower()}"
            elif key.startswith("!CodeForces"):
                pid = key[11:].strip()
                src_url = f"https://github.com/vEnhance/evan-learns-ioi/tree/main/CodeForces/{pid}"
                url = f"https://codeforces.com/contest/{pid[:-1]}/problem/{pid[-1]}"
            elif key.startswith("!Kattis"):
                pid = key[7:].strip().lower().replace(" ", "")
                src_url = f"https://github.com/vEnhance/evan-learns-ioi/tree/main/Kattis/{pid}"
                url = f"https://open.kattis.com/problems/{pid}"
            else:
                url = None
                src_url = None
            key = "💻" + key[1:]
        else:
            # HACK: empty string should be convert backed into None at this step
            url = url_dict.get(key) or None
            basename = f"Ep{int(n):03d}" + "-"
            basename += key.replace(" ", "-").replace("/", "-").replace(".", "-")
            basename += "-Solution"
            if key in url_dict:
                pdf_url = f"twitch/{basename}.pdf"
                src_url = f"twitch/{basename}.tex"
                src_type = "tex"
            else:
                pdf_url = None
                src_url = None
                src_type = None

        out += "<tr>"
        out += f"<td>Ep {n}</td>"
        if url is not None:
            out += f'<td><a href="{url}">{key}</a></td>'
        else:
            out += f"<td>{key}</td>"
        if pdf_url is not None:
            out += f'<td><a href="{escape(pdf_url)}">(pdf)</a></td>'
        else:
            out += "<td></td>"
        if src_url is not None:
            out += f'<td><a href="{escape(src_url)}">({src_type})</a></td>'
        else:
            out += "<td></td>"
        if youtube_url:
            out += f'<td><a href="{escape(youtube_url)}">(video)</a></td>'
        else:
            out += "<td></td>"
        out += "</tr>" + "\n"

    out += "</table>"
    return out


def get_card_trick() -> str:
    option_string = r"""<option value="{value}">{value}</option>"""
    ranks = [
        "...",
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    suits = ["...", "♣Clubs", "♦Diamonds", "♥Hearts", "♠Spades"]
    out = ""
    for n in range(4):
        out += f"<h2>Card {n + 1}</h2>" + "\n"
        out += r'<div class="container trick-container">' + "\n"
        out += f'<select class="rank-select" id="rank-{n}">' + "\n"
        for r in ranks:
            out += option_string.format(type="rank", name=n, value=r) + "\n"
        out += r"</select>" + "\n"
        out += f'<select class="suit-select" id="suit-{n}">' + "\n"
        for s in suits:
            out += option_string.format(type="suit", name=n, value=s) + "\n"
        out += r"</select>" + "\n"
        out += r"</div>" + "\n"
        out += r"<hr />" + "\n"

    out += r"<h2>Card 5</h2>" + "\n"
    out += r'<h1 id="answer">...</h1>' + "\n"
    out += r'<button type="button" class="btn" id="trick-button"></button>' + "\n"
    out += (
        r'<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slim-select@latest/dist/slimselect.min.css" />'
        + "\n"
    )
    out += (
        r'<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slim-select@latest/dist/slimselect.min.js"></script>'
        + "\n"
    )
    out += r'<script type="text/javascript" src="/static/js/trick.js"></script>' + "\n"
    return out


def faq(label: str, question: str) -> str:
    return (
        f'<a id="{label}" href="#{label}" style="color:#004824;">{label}.</a> {question}'
        f'<a href="#{label}" class="hash-link">#</a>'
    )


def hl(link: str, text: str) -> str:
    return f'<a id="{link}"></a>{text}<a href="#{link}" class="hash-link">#</a>'


def tshirt(year: str, alt: str | None = None, ext=".png") -> str:
    location = f"static/mop/shirts/{year}{ext}"
    if alt is None:
        alt = f"{year}."
    return (
        f'<a href="{location}" title="{alt}" class="tshirt-link">'
        f'<img src="{location}" alt="{alt}" class="tshirt" /></a>'
    )


def clickable_selfie_image(basename: str, alt: str) -> str:
    image_path = "static/headshots/" + basename + "-full.jpg"
    thumb_path = "static/headshots/" + basename + "-thumb.jpg"
    return f'<a href="{image_path}"><img src="{thumb_path}" alt="{alt}" /></a>'


def clickable_asy_image(basename: str) -> str:
    image_path = "static/asy-gallery/" + basename + ".png"
    thumb_path = image_path
    alt = basename
    return f'<a href="{image_path}"><img src="{thumb_path}" alt="{alt}" /></a>'


def year_chooser(classes: str, url_pattern: str, start: int, end: int) -> str:
    s = f'<div class="{classes}"><ul>\n'
    for year in range(end, start - 1, -1):
        url = url_pattern.format(year=year)
        s += f'<li><a href="{url}">{year}</a></li>\n'
    s += "</ul></div>"
    return s


def chooser_link(dirname: str, header_str: str) -> str:
    s = r'<div class="chooser empty-chooser"></div>' + "\n"
    paths = list(Path(dirname).glob("*.md"))
    assert len(paths) > 0, Path(dirname)
    paths.sort()
    paths.reverse()
    for p in paths:
        s += (
            f'<div data-year="{p.stem}" data-header="{header_str % p.stem}" class="hidden">'
            + "\n"
        )
        with open(p) as f:
            s += _md.render(f.read())
        s += "</div>" + "\n"
    return s


@functools.cache
def _opal_hunts() -> dict[str, list[dict]]:
    """The per-puzzle data for every public OPAL hunt, in unlock order, as
    written by gen-opaldata.py in the OPAL repository."""
    with open(OPAL_JSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def opal(hunt_slug: str, label: str | None = None) -> str:
    """Print one hunt's puzzle list, plus the data that opal-checker.js grades
    and hints from. The label names the hunt in the hint dropdown."""
    hunts = _opal_hunts()
    if hunt_slug not in hunts:
        raise KeyError(f"No hunt {hunt_slug!r} in {OPAL_JSON_PATH}")
    puzzles = hunts[hunt_slug]
    # < can't appear outside a JSON string, so escaping it is enough to keep the
    # blob from ever closing its own <script> early
    data_json = json.dumps(puzzles, ensure_ascii=False).replace("<", "\\u003c")
    return _component_env.get_template("opal-list.html.j2").render(
        slug=hunt_slug,
        label=label or hunt_slug,
        puzzles=puzzles,
        data_json=data_json,
    )


def opal_checker() -> str:
    return _component_env.get_template("opal-checker.html.j2").render()
