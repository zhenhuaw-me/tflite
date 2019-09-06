#!/bin/sh


EXIT_ON_ERROR() {
  echo "Error: ${1}" > /dev/stderr
  echo $? > /dev/stderr
  if [ $? -ne 0 ]; then
    echo "Error: ${1}" > /dev/stderr
    exit 1
  else
    echo "123 " > /dev/stderr
  fi
}

version=r1.14

schema_path="3rdparty/tflite_schema/schema.fbs"

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
# commit the schema change
git add ${schema_path}
git commit -m "schema: update fbs to ${version}"


