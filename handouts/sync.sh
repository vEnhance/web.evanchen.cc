#!/usr/bin/env bash
set -euxo pipefail

rclone sync -v . web:handouts \
  --exclude '\.gitignore' \
  --exclude 'sync.sh' \
  --exclude '*.pkl' \
  --exclude '*.{aux,bbl,bcf,blg,brf,fdb_latexmk,fls,log,out,nav,pre,pytxcode,pytxmcr,pytxpyg,run.xml,snm,toc,synctex.gz,jpg}' \
  --exclude '*-[0-9].{asy,pdf}' \
  --exclude '*-[0-9][0-9].{asy,pdf}'
