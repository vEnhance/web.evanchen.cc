#!/bin/bash

gsutil -m rsync -r \
  -x '\.gitignore$|sync\.sh$|.*\.pkl$|.*\.(aux|bbl|bcf|blg|brf|fdb_latexmk|fls|log|out|nav|pre|pytxcode|pytxmcr|pytxpyg|run\.xml|snm|toc|synctex\.gz|jpg|png)$|.*-[0-9][0-9]?\.(asy|pdf)$' \
  . gs://web.evanchen.cc/handouts/
