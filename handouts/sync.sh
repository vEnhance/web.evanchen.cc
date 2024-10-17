#!/usr/bin/env bash
set -euxo pipefail

gcloud storage rsync --recursive \
  --exclude '\.gitignore$|sync\.sh$|.*\.pkl$|.*\.(aux|bbl|bcf|blg|brf|fdb_latexmk|fls|log|out|nav|pre|pytxcode|pytxmcr|pytxpyg|run\.xml|snm|toc|synctex\.gz|jpg)$|.*-[0-9][0-9]?\.(asy|pdf)$' \
  --cache-control="private,max-age=0" \
  . gs://web.evanchen.cc/handouts
