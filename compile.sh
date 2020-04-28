#!/bin/bash

if [ $# -eq 0 ]; then
	python poole/poole.py -b --base-url=//web.evanchen.cc
elif [ $1 = "-debug" ]; then
	python poole/poole.py -b --base-url=https://web.evanchen.cc
elif [ $1 = "-local" ]; then
	python poole/poole.py -b --base-url=file:///home/evan/Dropbox/Documents/www/
else
	echo "huh?"
fi
