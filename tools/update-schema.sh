#!/bin/sh

# which version?
read -p "Which version of TensorFlow would you like to obtain the schema (\"v1.14.0\" for example): " version
if [ -z ${version} ]; then
  exit 1
fi
read -p "Going to obtain schema from version \"${version}\", continue? [Y|N] " input_str
if [ -z ${input_str} -o "${input_str}" != "Y"  ]; then
  exit 0
fi


# If you don't have a flatbuffers complier, you may build one with guide:
# https://google.github.io/flatbuffers/flatbuffers_guide_building.html
FBSC=~/toolchain/flatbuffers/flatbuffers/build/flatc

root_dir=$(dirname $(dirname $(readlink -f $0})))

schema_path="${root_dir}/3rdparty/schema.fbs"
output_path="${root_dir}/tflite"

# download schema.fbs
repo_tree='https://raw.githubusercontent.com/tensorflow/tensorflow'
file_path='tensorflow/lite/schema/schema.fbs'
url="${repo_tree}/${version}/${file_path}"
echo "Now, downloading from ${url}"
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

# commit the schema change?
echo "The diff of built out python module"
echo $(git diff)
read -p "Going to create a commit for these changes, continue? [Y|N] " input_str
if [ -z ${input_str} -o "${input_str}" != "Y"  ]; then
  exit 0
fi
git add ${schema_path} ${output_path}/tflite
git commit -m "update schema.fbs and tflite module to ${version}"
