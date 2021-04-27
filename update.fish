#!/bin/fish

./compile.sh > /dev/null

git diff --quiet

if test $status -eq 1
	echo "hi"
	git status -s
	gsutil cp (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
else
	gsutil cp (git show HEAD --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git show HEAD --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
end
