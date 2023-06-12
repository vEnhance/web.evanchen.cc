import csv
import datetime
import json
from pathlib import Path

from git.repo import Repo

repo = Repo(Path(__file__).parent, search_parent_directories=True)
tree = repo.heads.main.commit.tree

GITHUB_BASE = "https://github.com/vEnhance/web.evanchen.cc"


def handout_link(name, filename=None):
    filename = filename or name
    return (
        f'<a href="handouts/{name}/{filename}.pdf">(pdf)</a>'
        " "
        f'<a href="handouts/{name}/{filename}.tex">(tex)</a>'
        "<br>"
    )


def page_footer(page) -> str:
    input_name: str = page["url"].replace(".html", ".md")
    input_path = Path("input") / input_name
    try:
        blob = tree[str(input_path)]
    except KeyError:
        return (
            f'<div class="text-muted">View the <a href="{GITHUB_BASE}">source repository</a>.</div>'
            "\n"
            '<div class="font-italic text-muted">This hidden page not under public version control.</div>'
        )
    else:
        commit = next(repo.iter_commits(paths=blob.path, max_count=1))
        last_update_dt = datetime.datetime.utcfromtimestamp(commit.committed_date)
        last_update_str = last_update_dt.strftime("%a %-d %b %Y, %H:%M:%S UTC")
        return (
            "<div>"
            f'<a href="{GITHUB_BASE}">Source repository (git)</a> &bullet; '
            f'<a href="{GITHUB_BASE}/commits/main/{input_path}">Revision history</a> &bullet; '
            f'<a href="{GITHUB_BASE}/edit/main/{input_path}">Suggest edit</a>'
            r"</div>"
            f'<div class="text-muted">Updated {last_update_str} by '
            f'<a href="{GITHUB_BASE}/commit/{commit.hexsha}"><code>{commit.hexsha[0:12]}</code></a>'
            r"</div>"
        )


def get_twitch_table():
    tsv_path = Path.home() / "ProGamer/Writeups/data.tsv"
    json_path = Path.home() / "youtube-tex/urls.json"
    if not json_path.exists() or not tsv_path.exists():
        return "(Error: could not read Twitch table)"
    # TODO: static versions in data/ as fallback I guess

    with open(json_path) as f:
        url_dict = json.load(f)

    data = []
    with open(tsv_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            data.append(row)

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
        youtube = row["YouTube"]

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
            url = url_dict.get(key, None)
            basename = "Ep%03d" % int(n) + "-"
            basename += key.replace(" ", "-").replace("/", "-").replace(".", "-")
            basename += "-Solution"
            basename_tex = basename + ".tex"
            basename_pdf = basename + ".pdf"
            filename = Path.home() / "youtube-tex" / basename_tex
            if filename.exists():
                pdf_url = f"twitch/{basename_pdf}"
                src_url = f"twitch/{basename_tex}"
                src_type = "tex"
            else:
                pdf_url = None
                src_url = None
                src_type = None

        out += "<tr>"
        out += "<td>Ep %s</td>" % n
        if url is not None:
            out += '<td><a href="%s">%s</a></td>' % (url, key)
        else:
            out += "<td>%s</td>" % key
        if pdf_url is not None:
            out += f'<td><a href="{pdf_url}">(pdf)</a></td>'
        else:
            out += "<td></td>"
        if src_type is not None:
            out += f'<td><a href="{src_url}">({src_type})</a></td>'
        else:
            out += "<td></td>"
        if youtube:
            out += '<td><a href="%s">(video)</a></td>' % youtube
        else:
            out += "<td></td>"
        out += "</tr>" + "\n"

    out += "</table>"
    return out


def get_card_trick():
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
    for n in range(0, 4):
        out += f"<h2>Card {n+1}</h2>" + "\n"
        out += r'<div class="container trick-container">' + "\n"
        out += f'<select class="form-select rank-select" id="rank-{n}">' + "\n"
        for r in ranks:
            out += option_string.format(type="rank", name=n, value=r) + "\n"
        out += r"</select>" + "\n"
        out += f'<select class="form-select suit-select" id="suit-{n}">' + "\n"
        for s in suits:
            out += option_string.format(type="suit", name=n, value=s) + "\n"
        out += r"</select>" + "\n"
        out += r"</div>" + "\n"
        out += r"<hr />" + "\n"

    out += r"<h2>Card 5</h2>" + "\n"
    out += r'<h1 id="answer">...</h1>' + "\n"
    out += r'<button type="button" class="btn" id="trick-button"></button>' + "\n"
    out += r'<script type="text/javascript" src="/static/trick.min.js"></script>' + "\n"
    out += (
        r'<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>'
        + "\n"
    )
    out += r'<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" />'
    return out


def faq(label, question):
    return (
        f'<a id="{label}" href="#{label}" style="color:#004824;">{label}.</a> {question}'
        f'<a href="#{label}" class="hash-link">#</a>'
    )


def hl(link, text):
    return f'<a id="{link}"></a>{text}<a href="#{link}" class="hash-link">#</a>'


def tshirt(year, alt=None, ext=".png"):
    location = f"static/mop/shirts/{year}{ext}"
    if alt is None:
        alt = f"{year}."
    return (
        f'<a href="{location}" title="{alt}" class="tshirt-link">'
        f'<img src="{location}" alt="{alt}" class="tshirt" /></a>'
    )
