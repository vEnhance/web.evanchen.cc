#!/bin/fish

./compile.sh | tail -n 1

git diff --quiet

if test $status -eq 1 -a -z "$argv[1]"
	set_color --bold green
	echo "Using working state..."

	set_color normal
	git -c color.status=always status -s | grep -e "^" -e "[^ ]*.mkd"
	set_color cyan
	echo "------------------------------"
	set_color normal

	git status -s | grep -o "[^ ]*.mkd" > /dev/null
	if test $status -eq 1
		echo "No mkd files found"
		exit
	end
	gsutil -m cp (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git status -s | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
else
	set --local commit "$argv[1]"
	if test -z "$commit"
		set commit "HEAD"
	end
	set_color --bold green
	echo "Using commit" "$commit"

	set_color normal
	git show $commit --format=oneline --name-only --color=always \
		| grep -e "^" -e "[^ ]*.mkd"
	set_color cyan
	echo "------------------------------"
	set_color normal

	git show $commit --format=oneline --name-only | grep -e "[^ ]*.mkd" > /dev/null
	if test $status -eq 1
		echo "No mkd files found"
	else
		gsutil -m cp (git show $commit --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
		gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' (git show $commit --format=oneline --name-only | grep -o "[^ ]*.mkd" | sed s/.mkd\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
	end
end
