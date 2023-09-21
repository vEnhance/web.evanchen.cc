#!/bin/bash

gsutil -m rsync -r \
  -x '\.gitignore|sync\.sh$|pythontex_data\.pkl$|.*\.(aux|bbl|bcf|blg|brf|fdb_latexmk|fls|log|out|pre|pytxcode|pytxmcr|pytxpyg|run\.xml|toc|synctex\.gz)$|.*-[0-9][0-9]?\.(asy|pdf)$' \
  . gs://web.evanchen.cc/handouts/
