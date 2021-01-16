#!/bin/bash

if [ "$(uname -s)" == "Darwin" ]; then
  root_dir=$(dirname $(dirname $(greadlink -f $0})))
else
  root_dir=$(dirname $(dirname $(readlink -f $0})))
fi

# build and install the package
${root_dir}/tools/4-build.sh
pip install -U ${root_dir}/assets/dist/tflite-*.whl

echo -e "\nTesting: original import..."
python ${root_dir}/tests/test_original_import.py
if [ $? -ne 0 ]; then
  echo "FAIL!"
  exit 1
else
  echo "PASS!"
fi

echo -e "\nTesting: easy import..."
python ${root_dir}/tests/test_easy_import.py
if [ $? -ne 0 ]; then
  echo "FAIL!"
  exit 1
else
  echo "PASS!"
fi

echo -e "\nTesting: mobilenet example..."
python ${root_dir}/tests/mobilenet_example.py
if [ $? -ne 0 ]; then
  echo "FAIL!"
  exit 1
else
  echo "PASS!"
fi
