#!/bin/bash

set -euo pipefail

readarray -t MARKDOWN_FILES_ARRAY < <(git ls-files '*.md')
readarray -t SPELL_FILES_ARRAY < <(git ls-files)

echo "Running prettier..."
prettier --check "${MARKDOWN_FILES_ARRAY[@]}"

echo "Running spellcheck..."
codespell "${SPELL_FILES_ARRAY[@]}"

echo "Running htmlhint..."
htmlhint output/*.html

echo "✅ All OK!"
