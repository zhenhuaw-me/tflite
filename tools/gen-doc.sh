#!/bin/bash

if [ "$(uname -s)" == "Darwin" ]; then
  root_dir=$(dirname $(dirname $(greadlink -f $0})))
else
  root_dir=$(dirname $(dirname $(readlink -f $0})))
fi
doc_dir=${root_dir}/docs
proj_dir=${root_dir}/tflite

rm -rf ${doc_dir}
pdoc --overwrite --html --html-dir ${doc_dir} ${proj_dir} tflite
mv ${doc_dir}/tflite/* ${doc_dir}
rmdir ${doc_dir}/tflite

