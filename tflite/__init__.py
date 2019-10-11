# making the nested call fine to use, where `tflite.tflite` IS-A `tflite`.
from . import tflite

# making the interface easy to use
from .tflite.Model import *
