#!/bin/sh

set -euxo

mkdir thumbnails
for i in ./*-full.jpg; do
  magick -thumbnail 128 "$i" "thumbnails/$i"
done

cd thumbnails
rename full thumb ./*.jpg
mv ./*.jpg ..
cd ..
rmdir thumbnails
