#!/bin/bash

set -euo pipefail

htmlhint output/*.html
./scripts/broken-links.py

echo "✅ All OK!"
