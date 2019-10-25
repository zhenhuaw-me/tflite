The python package to parse TFLite models
=========================================

TFLite models (`*.tflite`) are in [FlatBuffers](https://google.github.io/flatbuffers/) format. This `tflite` package is built to parse the TFLite models from the `schema.fbs` of [TensorFlow](https://github.com/tensorflow/tensorflow).

## Usage

Using this package, you can parse the TFLite models (`*tflite`) in Python. One target of this package is to let people use it as the one originally built from `schema.fbs`.

This package has been published on [pypi.org](https://pypi.org/project/tflite/), `pip install tflite` will install. Basically, the usage styles include:

* **Easy import** avoids too many imports per submodules ([example](tests/test_easy_import.py)): `import tflite`. This is also the recommanded way to use this package.
* **Nested import** tflite modules `tflite.tflite` as it is the originally built one ([example](tests/test_nested_import.py)): `from tflite.tflite.Model import Model`. This is as a workaround when encountering bug in easy import.

The *easy import* imports the classes and functions of one submodules into top module directly, e.g. import the `{package}.{submodules}.{class or function}` as `{package}.{class or function}`. For example, when building the `Model` object, `tflite.Model.GetRootAsModel(buf, 0)` should be used rather than `tflite.Model.Model.GetRootAsModel(buf, 0)`. This should be much easy to use. Look into the [tests](tests) for more examples.

The package is versioning mirrored to [TensorFlow package](https://pypi.org/project/tensorflow/), which means a `tflite==1.14.0` is generated from `tensorflow==1.14.0`. Versions after `1.14.0` is maintained.

Besides, if you prefer the *very original* style of the FlatBuffers generated package, try [this one](https://github.com/FrozenGene/tflite).


## Development

To develop this package, additional depdendency can be installed via `pip install -r requirements.txt`.

The [`tools`](tools) directory holds some scripts to update the package to corresponding TensorFlow version. There are three steps currently:
1. [Download](tools/update-schema.sh) the `schema.fbs` change of a version.
2. [Update](tools/update-importing.py) the classes and functions import of submodules.
3. Update the versioning in [setup.py](setup.py).
4. Build and [Test](tests) around.
5. [Upload](tools/build-and-upload.sh) the package to PyPI.

Features could be added to make the parsing easy in the future.

Don't forget to re-install the newly built `tflite` package before testing it. You may also try `source tools/source-me.sh` rather than the annoying build and install process in development.


## Resources

* [GitHub](https://github.com/jackwish/tflite) of this package.
* [Converting TensorFlow model to TFLite model](https://www.tensorflow.org/lite/convert).
* [This TFLite package](https://github.com/FrozenGene/tflite) is used in [TVM](https://tvm.ai/).


## License

Apache License Version 2.0 as TensorFlow's.


## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly, which could be property of Google. Maitainer of this package has tried to [contact](assets/[TFLite] Propose to maintain a PyPI package for TFLite model parsing.eml) [one](https://github.com/aselle) of the TensorFlow maitainers for legal or permission issues, but receiving no reply. Ownership or maitainship of this package is open to transfer or close if there were any issues.
