#!/bin/bash

set -euo pipefail

python3 build.py

# reformat output with tidy
tidy -config ./tidyrc -qm ./output/*.html

# reformat it with prettier afterwards
prettier -w ./output/*.html

# Lint everything
./scripts/lint.sh
