#!/bin/bash

set -e

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

# pass the version in either via `--version v2.11.0`
while [[ $# -gt 0 ]]; do
  case $1 in
    --version)
      version="$2"
      shift # past argument
      shift # past value
      ;;
    *)
      POSITIONAL_ARGS+=("$1") # save positional arg
      shift # past argument
      ;;
  esac
done

if [ -z "$version" ]; then
  echo "Missing --version"
  exit 1
fi

if [[ $version != v* ]]; then
  echo "--version should start with v (e.g. v2.11.0)"
  exit 1
fi

cd $SCRIPTPATH/..

docker build -t zhenhuaw-me-tflite .
docker run --rm -it -v $PWD:/app zhenhuaw-me-tflite /bin/bash -c "\
    scripts/update-schema.sh --version $version --no-commit && \
    python3 scripts/gen-op-list.py --no-commit && \
    python3 scripts/update-importing.py --no-commit && \
    scripts/gen-doc.sh && \
    scripts/update-init-py-version.sh --version $version && \
    scripts/build-wheel.sh && \
    \
    pip3 uninstall -y tflite && \
    pip3 install ./assets/dist/tflite-*-py2.py3-none-any.whl && \
    pytest"
