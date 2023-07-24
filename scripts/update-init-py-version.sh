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

# if the version is passed in as v1.2.3 then cut off the first character
if [[ $version = v* ]]; then
  version="${version:1}"
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
  SEDCMD="sed -i '' -e"
  LC_CTYPE=C
  LANG=C
else
  SEDCMD="sed -i -e"
fi

$SEDCMD "3s/.*/__version__ = \'$version\'/" $SCRIPTPATH/../tflite/__init__.py
