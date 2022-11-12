Easily Parse TFLite Models with Python
======================================

![Build and Test](https://github.com/zhenhuaw-me/tflite/workflows/Build%20and%20Test/badge.svg)

This [`tflite` package](https://pypi.org/project/tflite/) parses TensorFlow Lite (TFLite) models (`*.tflite`), which are built by [TFLite converter](https://www.tensorflow.org/lite/convert). For background, please refer to [Introducing TFLite Parser Python Package](https://zhenhuaw.me/blog/2020/introducing-tflite-parser-package.html).


## Usage

Install the package and use it like what you build from the TensorFlow codebase.
It's recommended to install the version that same as the TensorFlow that generates the TFLite model.

```sh
pip install tensorflow==2.3.0
pip install tflite==2.3.0
```

The raw API of `tflite` can be found in [this documentation](https://zhenhuaw.me/tflite/docs/).
The [MobileNet test](tests/test_mobilenet.py) can serve as a usage example of parsing models.


## Enhancements

The generated python package is not friendly to use sometimes.
We have introduced several enhancements:

* **Easy import**: A single `import tflite` ([example](https://github.com/zhenhuaw-me/tflite/blob/master/tests/test_mobilenet.py)) to replace importing every classes and funtions in `tflite` ([example](tests/test_original_import.py)).
* **Builtin opcode helper**: The opcode is _encoded_ as digits which is hard to parse for human. Two APIs added to make it easy to use.
  * [`tflite.opcode2name()`](https://github.com/zhenhuaw-me/tflite/blob/master/tflite/utils.py#L1): get the type name of given opcode.
  * [`tflite.BUILTIN_OPCODE2NAME`](https://github.com/zhenhuaw-me/tflite/blob/master/tflite/utils.py#L9): a dict that maps the opcode to name of all the builtin operators.


## Compatibility Handling

TensorFlow sometimes leaves compability hanlding of the TFLite model to the users.
As these are API breaking change that can be easily fixed, we do this in the `tflite` package.

* [`tflite.OperatorCode.BuiltinCode()`](https://github.com/zhenhuaw-me/tflite/blob/master/tflite/OperatorCode.py#L43): maintains API compability in `2.4.0`, see [this issue](https://github.com/tensorflow/tensorflow/issues/46663).


## Contributing Updates

As the operator definition may change across different TensorFlow versions, this package needs to be updated accordingly. If you notice that the package is out of date, please feel free to contribute new versions. This is pretty simple, instructions as below.

1. [Fork the repository](https://help.github.com/en/github/getting-started-with-github/fork-a-repo), and download it.
2. Install additional depdendency via `pip install -r requirements.txt`. And install [flatbuffer compiler](https://google.github.io/flatbuffers/flatbuffers_guide_using_schema_compiler.html) (you may need to [manually build it](https://google.github.io/flatbuffers/flatbuffers_guide_building.html)).
3. Generate the code for update. Tools have been prepared, there are prompt for actions.
    1. [Download](scripts/update-schema.sh) `schema.fbs` for a new version.
    2. [Update](scripts/gen-op-list.py) the builtin operator mapping.
    3. [Update](scripts/update-importing.py) the classes and functions import of submodules.
    4. [Update](scripts/gen-doc.sh) the API document.
    5. Update the versioning in [`__init__.py`](tflite/__init__.py).
    6. [Build](scripts/build-wheel.sh) and [test](tests) (simply `pytest`) around. Don't forget to re-install the newly built `tflite` package before testing it.
4. Push your change and open [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
5. The maintainer will take the responsibility to upload change to PyPI when merged.


## Resources

* [PyPI page](https://pypi.org/project/tflite/).
* [GitHub page](https://github.com/zhenhuaw-me/tflite).
* [Module list](https://zhenhuaw.me/tflite/docs).
* [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert).


## License

Apache License Version 2.0 as TensorFlow's.


## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly. Maintainer of this package had tried to [contact](assets/disclaimer.eml) TensorFlow maintainers for licensing issues, but received no reply. Ownership or maintainship is open to transfer or close if there were any issue.
