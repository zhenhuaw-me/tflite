#!/bin/sh

if [ $# -ne 1 ]; then
  echo "Usage: update-schema.sh [TensorFlow Version]"
  echo "    Download schema and generate python module"
  echo "Note: you may need to change the flatbuffers complier 'FBSC'"
  exit 1
fi

version=${1}

# If you don't have a flatbuffers complier, you may build one with guide:
# https://google.github.io/flatbuffers/flatbuffers_guide_building.html
FBSC=~/toolchain/flatbuffers/flatbuffers/build/flatc

schema_path="3rdparty/tflite_schema/schema.fbs"
output_path="python/tflite_parser"

# download schema.fbs
repo_tree='https://raw.githubusercontent.com/tensorflow/tensorflow'
file_path='tensorflow/lite/schema/schema.fbs'
url="${repo_tree}/${version}/${file_path}"
curl ${url} -o "${schema_path}"

# exit?
if [ $(grep -q "404: Not Found" ${schema_path}) ]; then
  echo "Error: fail to download schema from ${url}"
  exit 1
fi
changed_lines=$(git diff ${schema_path} | wc -l)
if [ ${changed_lines} -eq 0 ]; then
  echo "No change to schema, exit!"
  exit 0
fi

echo "Building flatbuffers python module in ${output_path}"
${FBSC} --python -o ${output_path} ${schema_path}

# commit the schema change
git add ${schema_path} ${output_path}/tflite
git commit -m "update schema.fbs and tflite module to ${version}"
