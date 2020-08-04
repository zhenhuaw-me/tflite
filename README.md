Easily Parse TFLite Models with Python
======================================

![Build and Test](https://github.com/jackwish/tflite/workflows/Build%20and%20Test/badge.svg)

This [`tflite` package](https://pypi.org/project/tflite/) parses TensorFlow Lite (TFLite) models (`*.tflite`), which are built by [TFLite converter](https://www.tensorflow.org/lite/convert). For background, please refer to [Introducing TFLite Parser Python Package](https://jackwish.net/2020/introducing-tflite-parser-package.html).


## Usage

### Installation

```sh
pip install tensorflow==1.14.0
pip install tflite==1.14.0.post1
```

It would be better if use a correct version regarding tensorflow, where the mapping is as below.
Since `2.0.1`, the `.post[?]` suffix is not needed, such that we can keep this version map simple.
If you notice that some version is missing, please consider [contribute it](#contributing-updates)! :)

| TensorFlow package version   | tflite package version |
|------------------------------|------------------------|
|      1.14.0                  |      1.14.0.post1      |
|      1.15.0                  |      1.15.0.post1      |
|      1.15.2                  |      1.15.2            |
|      2.0.0                   |      2.0.0.post2       |
|      2.0.1                   |      2.0.1             |
|      2.1.0                   |      2.1.0             |


### Import the package

The package can be imported with *easy import* or *original import*, where the difference is how many `import` you write - no functionality divergence. For supported interfaces, please refer to [document page](https://jackwish.net/tflite/docs/).

**Easy Import (Recommanded)**

*Easy import* enables parsing by one single `import tflite`. This is achieved by importing classes and functions of one submodules into top module [directly](tflite/__init__.py).

[MobileNet parsing example](https://github.com/jackwish/tflite/blob/master/tests/test_mobilenet.py) shows how to parse model with `import tflite` **ONLY ONCE**.

**Original Import**

You can use this package just like the newly FlatBuffers generated one ([example](tests/test_original_import.py)) to avoid any break of your legacy code.

```python
from tflite.Model import Model
```


## Contributing Updates

As the operator definition may change across different TensorFlow versions, this package needs to be updated accordingly. If you notice that the package is out of date, please feel free to contribute new versions. This is pretty simple, instructions as below.

1. [Fork the repository](https://help.github.com/en/github/getting-started-with-github/fork-a-repo), and download it.
2. Install additional depdendency via `pip install -r requirements.txt`. And install [flatbuffer compiler](https://google.github.io/flatbuffers/flatbuffers_guide_using_schema_compiler.html) (you may need to [manually build it](https://google.github.io/flatbuffers/flatbuffers_guide_building.html)).
3. Generate the code for update. Tools have been prepared, there are prompt for actions.
    1. [Download](tools/1-update-schema.sh) `schema.fbs` for a new version.
    2. [Update](tools/2-update-importing.py) the classes and functions import of submodules.
    3. Update the versioning in [setup.py](setup.py).
    4. [Build](tools/3-build.sh) and [Test](tests) (simply `pytest`) around. Don't forget to re-install the newly built `tflite` package before testing it.
4. Push your change and open [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
5. The maintainer will take the responsibility to upload change to PyPI when merged.


## Resources

* [PyPI page](https://pypi.org/project/tflite/).
* [GitHub page](https://github.com/jackwish/tflite).
* [Module list](https://jackwish.net/tflite/docs).
* [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert).


## License

Apache License Version 2.0 as TensorFlow's.


## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly. Maintainer of this package had tried to [contact](assets/disclaimer.eml) TensorFlow maintainers for licensing issues, but received no reply. Ownership or maintainship is open to transfer or close if there were any issue.
