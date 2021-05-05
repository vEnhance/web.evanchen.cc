#!/bin/fish

./compile.sh | tail -n 1
echo "Compiled"

git diff --quiet

if test $status -eq 1 -a -z "$argv[1]"
	echo "Using working state..."
	git status -s | grep -o "[^ ]*.mkd"
	if test $status -eq 1
		echo "No mkd files found"
		exit
	end
	gsutil -m cp (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
else
	set --local commit "$argv[1]"
	if test -z $commit
		set commit "HEAD"
	end
	echo "Using commit " $commit
	git show $commit --format=oneline --name-only | grep -o "[^ ]*.mkd"
	if test $status -eq 1
		echo "No mkd files found"
	else
		gsutil -m cp (git show $commit --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
		gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git show $commit --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
	end
end
echo "Make sure no leek"
echo $commit
