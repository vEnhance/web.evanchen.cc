#!/bin/fish

./compile.sh

gsutil cp (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
