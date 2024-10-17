#!/bin/fish

./scripts/compile.sh
git diff --quiet

if test $status -eq 1 -a -z "$argv[1]"
    set_color --bold green
    echo "Using working state..."

    set_color normal
    git -c color.status=always status -s | grep -E "input/[^ ]*.md"
    set_color cyan
    echo ------------------------------
    set_color normal

    git status -s | grep -E -o "input/[^ ]*.md" >/dev/null
    if test $status -eq 1
        echo "No md files found"
        exit
    end
    gcloud storage cp (git status -s | grep -E -o "input/[^ ]*.md" | sed s/.md\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
    gcloud storage objects update --custom-metadata='Cache-Control="private,max-age=0"' (git status -s | grep -E -o "input/[^ ]*.md" | sed s/.md\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
else
    set --local commit "$argv[1]"
    if test -z "$commit"
        set commit HEAD
    end
    set_color --bold green
    echo "Using commit" "$commit"

    set_color normal
    git show $commit --format="" --name-only --color=always \
        | grep -E -e "input/[^ ]*.md"
    set_color cyan
    echo ------------------------------
    set_color normal

    git show $commit --format="" --name-only | grep -E "input/[^ ]*.md" >/dev/null
    if test $status -eq 1
        echo "No md files found"
    else
        gcloud storage cp (git show $commit --format="" --name-only | grep -E -o "input/[^ ]*.md" | sed s/.md\$/.html/ | sed s/^input/output/) gs://web.evanchen.cc/
        gcloud storage objects update --custom-metadata='Cache-Control="private,max-age=0"' (git status -s | grep -E -o "input/[^ ]*.md" | sed s/.md\$/.html/ | sed s/^input/gs:\\/\\/web.evanchen.cc/)
    end
end
