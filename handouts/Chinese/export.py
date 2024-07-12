#! /usr/bin/python3
import re

r = re.compile(r"[ \t]?\\ii\[([^\]]+)\]\{([a-z1-5]+)\} +([^\n\r\t]+)")
with open("Chinese.tex", "r", encoding="utf-8") as f, open(
    "out.txt", "w", encoding="utf-8"
) as g:
    for line in f:
        m = r.match(line.strip())
        if m:
            g.write(m.group(1) + ";" + m.group(2) + ";" + m.group(3) + "\n")
