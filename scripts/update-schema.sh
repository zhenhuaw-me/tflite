#!/bin/bash

set -e

POSITIONAL_ARGS=()

# pass the version in either via `--version v2.11.0`
while [[ $# -gt 0 ]]; do
  case $1 in
    --version)
      version="$2"
      shift # past argument
      shift # past value
      ;;
    --no-commit)
      NO_COMMIT=1
      shift # past argument
      ;;
    *)
      POSITIONAL_ARGS+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

# or if no arguments are passed in we prompt on the command line
if [ -z "$version" ]; then
  # which version?
  read -p "Which version of TensorFlow would you like to obtain the schema (\"v1.14.0\" for example): " version
  if [ -z ${version} ]; then
    exit 1
  fi
  read -p "Going to obtain schema from version \"${version}\", continue? [Y|N] " input_str
  if [ -z ${input_str} -o "${input_str}" != "Y"  ]; then
    exit 0
  fi
fi

if [ "$(uname -s)" == "Darwin" ]; then
  root_dir=$(dirname $(dirname $(greadlink -f $0})))
else
  root_dir=$(dirname $(dirname $(readlink -f $0})))
fi

schema_path="${root_dir}/3rdparty/schema.fbs"
output_path="${root_dir}"

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
rm -f ${root_dir}/tflite/*.py
FBSC=$(which flatc || true)
if [ ! -x "$FBSC" ]; then
  echo "Error: Flatbuffer complier doesn't exist! Build with https://google.github.io/flatbuffers/flatbuffers_guide_building.html"
  exit 1
fi
${FBSC} --python -o ${output_path} ${schema_path}
# revert the __init__.py
git checkout ${root_dir}/tflite/__init__.py
git checkout ${root_dir}/tflite/utils.py

# commit the schema change?
if [ "$NO_COMMIT" != 1 ]; then
  read -p "Going to create a commit for these changes, continue? [Y|N] " input_str
  if [ -z ${input_str} -o "${input_str}" != "Y"  ]; then
    exit 0
  fi
  git add ${schema_path} ${output_path}/tflite
  git commit -m "update schema.fbs and tflite module to ${version}"
fi
