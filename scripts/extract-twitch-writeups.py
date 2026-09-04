#!/usr/bin/python3

"""
Use only on von-enabled machines

(1) Reads problems.csv from TWITCH_DATA_DIR
(2) Writes ~/Freezer/youtube-tex/ with TeX files that you can compile
(3) Updates urls.lock (DO NOT EDIT MANUALLY but version control it)

To actually upload the TeX files, run upload-twitch-writeups.sh.
"""

import csv
from pathlib import Path

from von import api

TWITCH_DATA_DIR = Path(__file__).parent.parent / "data" / "twitch"
OUT_FOLDER = Path.home() / "Freezer" / "youtube-tex"

assert OUT_FOLDER.exists(), f"{OUT_FOLDER} does not exist on this computer"

with open(TWITCH_DATA_DIR / "problems.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)
url_dict: dict[str, str] = {}

LATEX_TEMPLATE = r"""\documentclass[11pt]{scrartcl}
\usepackage{evan}

\begin{document}
\title{%s}
\subtitle{Evan Chen}
\author{Twitch Solves ISL}
\date{Episode %d}
\maketitle

\section*{Problem}
%s

%s

%s

\newpage

\section*{Solution}
%s

\end{document}"""

for row in data:
    n = row["N"]
    key = row["Source"]
    youtube = row["YouTube"]

    if youtube:
        if "&" in youtube:
            short_url = youtube[: youtube.index("&")]
        else:
            short_url = youtube
        short_url = short_url.replace("_", r"\_").replace(
            "www.youtube.com/watch?v=", "youtu.be/"
        )
        video_tex = (
            r"\section*{Video}"
            + "\n"
            + rf"\href{{{youtube}}}{{\texttt{{{short_url}}}}}"
        )
    else:
        video_tex = ""
        short_url = ""

    if api.has(key):
        e = api.get(key)

        if e.url:
            external_tex = r"\section*{External Link}" + "\n" + r"\url{" + e.url + "}"
            url_dict[key] = e.url
        else:
            external_tex = ""
            url_dict[key] = ""

        tex = LATEX_TEMPLATE % (
            key,
            int(n),
            e.bodies[0],
            video_tex,
            external_tex,
            e.bodies[1],
        )
        basename = (
            f"Ep{int(n):03d}"
            + "-"
            + key.replace(" ", "-").replace("/", "-").replace(".", "-")
            + "-Solution"
            + ".tex"
        )
        filename = OUT_FOLDER / basename

        with open(filename, "w") as f:
            print(tex, file=f)
    elif key.startswith("!"):
        pass
    else:
        print(f"Ep{int(n):3d} MISSING VON {key}: {short_url}")
        continue


urls_path = TWITCH_DATA_DIR / "urls.lock"
with open(urls_path, "w") as f:
    print("# Auto-generated from problems.csv by extract-twitch-writeups.py", file=f)
    print("# DO NOT EDIT BY HAND", file=f)
    print("# vim: " + "readonly filetype=toml", file=f)
    print(file=f)
    for source, url in url_dict.items():
        # HACK: None is not a supported TOML type, so I cope with an empty string
        print(f'"{source}" = "{url or ""}"', file=f)
print(f"✅ Wrote URL dictionary to {urls_path}")
