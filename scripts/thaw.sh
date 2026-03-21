#!/bin/bash

if [ $# -eq 0 ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/*.html
elif [ "$1" = "-a" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/*.html gs://web.evanchen.cc/static/** gs://web.evanchen.cc/applets/**
elif [ "$1" = "-A" ]; then
  gcloud storage objects update --cache-control="private,max-age=0" gs://web.evanchen.cc/
else
  echo "huh?"
fi
