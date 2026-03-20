#!/bin/bash

set -euo pipefail

python3 poole/poole.py -b \
  --md-ext=extra \
  --md-ext=smarty \
  --md-ext=sane_lists \
  --md-ext=mdx_truly_sane_lists >/dev/null

# reformat output with tidy
tidy -config ./tidyrc -qm ./output/*.html

# reformat it with prettier afterwards
prettier -w ./output/*.html

# Lint everything
./scripts/lint.sh
