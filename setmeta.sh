#!/bin/bash

if [ $# -eq 0 ]; then
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/*.html
elif [ $1 = "-h" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.html
elif [ $1 = "-p" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.pdf
elif [ $1 = "-a" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/
else
	echo "huh?"
fi
