#!/bin/bash

set -euxo pipefail
asy -f pdf "$1" -o tmp.pdf
convert -density 300 -background white -alpha remove -alpha off tmp.pdf "${1%.asy}.png"
rm tmp.pdf
