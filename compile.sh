#!/bin/bash

if [ $# -eq 0 ]; then
	python poole/poole.py -b --base-url=//web.evanchen.cc
elif [ $1 = "-debug" ]; then
	python poole/poole.py -b --base-url=https://web.evanchen.cc
else
	echo "huh?"
fi
