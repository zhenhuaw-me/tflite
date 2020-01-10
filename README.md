Python Package to Parse TFLite Models Easily
============================================

![GitHub Action badge](https://github.com/jackwish/tflite/workflows/Build%20and%20Test/badge.svg)

TFLite models (`*.tflite`) are in [FlatBuffers](https://google.github.io/flatbuffers/) format. This `tflite` package is built to parse the TFLite models from the `schema.fbs` of [TensorFlow](https://github.com/tensorflow/tensorflow).


## Usage

Using this package, you can parse the TFLite models (`*.tflite`) in Python. One target of this package is to let people use it as the one originally built from `schema.fbs`. The module and submodules are listed in the [document page](https://jackwish.net/tflite/docs).

### Installation

This package can be installed via [pip](https://pypi.org/project/tflite/), and is versioning *similar* to [TensorFlow package](https://pypi.org/project/tensorflow/). And the version mapping is as below.

| TensorFlow package version   | tflite package version |
|------------------------------|------------------------|
|      1.14.0                  |      1.14.0.post1      |
|      1.15.0                  |      1.15.0.post1      |
|      2.0.0                   |      2.0.0.post2       |
|      2.1.0                   |      2.1.0             |

It would be better if you use a correct version, such as:

```sh
pip install tensorflow==1.14.0
pip install tflite==1.14.0.post1
```

### Easy Import

With this package, you may avoid too many imports per submodules. The *easy import* imports the classes and functions of one submodules into top module directly, e.g. import the `{package}.{submodules}.{class or function}` as `{package}.{class or function}`. For example, when building the `Model` object, `tflite.Model.GetRootAsModel(buf, 0)`.

```python
import tflite
# use tflite.Model
```

The [MobileNet parsing example](https://github.com/jackwish/tflite/blob/master/tests/mobilenet_example.py) shows how to parse model with `import tflite` **ONLY ONCE**. On contrary, the original generated package needs to import every classes by hand ([see this](https://github.com/apache/incubator-tvm/blob/v0.6.0/python/tvm/relay/frontend/tflite.py#L843-L849)) which is pretty annoying.

In addition, you can use this package just like the newly FlatBuffers generated one ([example](tests/test_original_import.py)):

```python
from tflite.Model import Model
# use Model
```

## Development

> Package users can safely ignore this part.

To develop this package, additional depdendency can be installed via `pip install -r requirements.txt`.

The [`tools`](tools) directory holds some scripts to update the package to corresponding TensorFlow version. There are steps:
1. [Download](tools/update-schema.sh) the `schema.fbs` change of a version.
2. [Update](tools/update-importing.py) the classes and functions import of submodules.
3. Update the versioning in [setup.py](setup.py).
4. [Build](tools/build.sh) and [Test](tests) around.
5. [Upload](tools/upload.sh) the package to PyPI.

Features could be added to make the parsing easy in the future.

Don't forget to re-install the newly built `tflite` package before testing it. You may also try `source tools/source-me.sh` rather than the annoying build and install process in development.


## Resources

* [GitHub page](https://github.com/jackwish/tflite) of this package.
* [Module list](https://jackwish.net/tflite/docs) of this package.
* [Converting TensorFlow model to TFLite model](https://www.tensorflow.org/lite/convert).
* [Another package](https://github.com/FrozenGene/tflite) has already been used in [TVM](https://tvm.ai).


## License

Apache License Version 2.0 as TensorFlow's.


## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly, which could be property of Google. Maintainer of this package had tried to [contact](assets/disclaimer.eml) TensorFlow maintainers for licensing issues, but received no reply. Ownership or maitainship of this package is open to transfer or close if there were any issues.
