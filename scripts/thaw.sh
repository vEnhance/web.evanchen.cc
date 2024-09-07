#!/bin/bash

if [ $# -eq 0 ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/*.html
elif [ "$1" = "-j" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**/*.js
elif [ "$1" = "-c" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**/*.css
elif [ "$1" = "-e" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/exams/*
elif [ "$1" = "-o" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/elmo/*
elif [ "$1" = "-s" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/static/*
elif [ "$1" = "-h" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**/*.html
elif [ "$1" = "-t" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**/*.tex
elif [ "$1" = "-p" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/**/*.pdf
elif [ "$1" = "-u" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/upload/** gs://web.evanchen.cc/private/** gs://web.evanchen.cc/textbooks/**
elif [ "$1" = "-a" ]; then
  PYTHONWARNINGS="ignore" gsutil -m setmeta -R -h 'Cache-Control:private, max-age=0, no-transform' gs://web.evanchen.cc/
else
  echo "huh?"
fi
