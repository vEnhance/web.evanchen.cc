#!/bin/bash

if [ $# -eq 0 ]; then
	gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/*.html gs://web.evanchen.cc/FAQs/*.html
elif [ $1 = "-c" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.css
elif [ $1 = "-e" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/exams/*
elif [ $1 = "-o" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/elmo/*
elif [ $1 = "-s" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/static/*
elif [ $1 = "-h" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.html
elif [ $1 = "-t" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.tex
elif [ $1 = "-p" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**.pdf
elif [ $1 = "-u" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/upload/*
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/private/*
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/textbooks/*
elif [ $1 = "-a" ]; then
	gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/
else
	echo "huh?"
fi
