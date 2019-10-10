The python package to parse TFLite models
=========================================

This `tflite` pip package is built from the `schema.fbs` of [TensorFlow](https://github.com/tensorflow/tensorflow) with [FlatBuffers](https://google.github.io/flatbuffers/).

## The Package

Using this package, you can parse the TFLite models (`*tflite`) in Python. One target of this package is to let people use it as the one originally built from `schema.fbs`. ~~The versions is managed mirrored with TensorFlow, e.g. `v1.14.0`, though only few versions are supported.~~ `v1.14.0` is the default supported version at this time.

### Installation

This package is published via [pypi.org](https://pypi.org/), `pip install tflite` will install it.

### Usage

Basically, you may use it as the one originally built from `schema.fbs`.

### Development

The [`tools`](tools) directory holds some scripts to update the package to corresponding TensorFlow version. Features could be added to make the parsing easy in the future.

## License

Apache License Version 2.0 as TensorFlow's.

## Disclaimer

The `schema.fbs` is obtained from TensorFlow directly, which could be property of Google. Maitainer of this package has tried to contact [one of the TensorFlow maitainers](https://github.com/aselle) for legal or permission issues, but receiving no reply. Ownership or maitainship of this package is open to transfer or close if there were any issues.
