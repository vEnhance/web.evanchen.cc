#!/bin/bash

if [ $# -eq 0 ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/*.html
elif [ "$1" = "-j" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/**/*.js
elif [ "$1" = "-c" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/**/*.css
elif [ "$1" = "-e" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/exams/*
elif [ "$1" = "-o" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/elmo/**
elif [ "$1" = "-s" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/static/*
elif [ "$1" = "-h" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/**/*.html
elif [ "$1" = "-t" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/**/*.tex
elif [ "$1" = "-p" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/**/*.pdf
elif [ "$1" = "-u" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/upload/** gs://web.evanchen.cc/private/** gs://web.evanchen.cc/textbooks/**
elif [ "$1" = "-a" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/
else
  echo "huh?"
fi
