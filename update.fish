#!/bin/fish

./compile.sh | tail -n 1
echo "Compiled"

git diff --quiet

if test $status -eq 1
	git status -s
	git status -s | grep -o "[^ ]*.mkd"
	if test $status -eq 1
		echo "No mkd files found"
		exit
	end
	gsutil cp (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
else
	git show HEAD --format=oneline --name-only
	git show HEAD --format=oneline --name-only | grep -o "[^ ]*.mkd"
	if test $status -eq 1
		echo "No mkd files found"
		exit
	end
	gsutil cp (git show HEAD --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git show HEAD --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
end
