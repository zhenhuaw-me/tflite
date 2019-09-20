#!/bin/bash

testRelease=1
if [ $# -ne 0 ]; then
  if [ ${1} == "Release" ]; then
    testRelease=0
  fi
fi

root_dir=$(dirname $(dirname $(readlink -f $0})))

python3 ${root_dir}/python/setup.py sdist bdist_wheel


python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
