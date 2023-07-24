#!/bin/bash

set -e

if [ "$(uname -s)" == "Darwin" ]; then
  root_dir=$(dirname $(dirname $(greadlink -f $0})))
else
  root_dir=$(dirname $(dirname $(readlink -f $0})))
fi
rm -f ${root_dir}/assets/dist/tflite-*.whl

# prefer python3/pip3 over python/pip
PYTHON=$(which python3 || which python || true)
PIP=$(which pip3 || which pip || true)

$PIP install build flatbuffers numpy

$PYTHON -m build --outdir ${root_dir}/assets/dist
rm -rf ${root_dir}/tflite.egg-info
rm -rf ${root_dir}/build
