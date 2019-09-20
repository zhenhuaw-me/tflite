#!/bin/bash

testRelease=1
if [ $# -ne 0 ]; then
  if [ ${1} = "Release" ]; then
    testRelease=0
  fi
fi

root_dir=$(dirname $(dirname $(readlink -f $0})))

python3 ${root_dir}/python/setup.py bdist_wheel \
  --bdist-dir ${root_dir}/assets/build \
  --dist-dir ${root_dir}/assets/dist
rm -rf tflite.egg-info

if [ ${testRelease} -eq 1 ]; then
  python3 -m twine upload \
    --repository-url https://test.pypi.org/legacy/ \
    ${root_dir}/assets/dist/tflite-*
else
  echo "will upload"
  python3 -m twine upload ${root_dir}/assets/dist/tflite-*
fi
