#!/bin/bash

set -euo pipefail

prek run -a

./scripts/compile.sh
htmlhint output/*.html
./scripts/broken-links.py

echo "✅ All OK!"
