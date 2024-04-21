#!/bin/bash

#check Makefile

if [ ! -f ../Makefile ]; then
  echo "Makefile not found!"
  exit 1
fi

# check for python3
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi

# This script is used to run the tester
python3 tester.py