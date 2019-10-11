import tflite
print(dir(tflite))
import tflite.tflite as tflite2
print(dir(tflite.tflite))
import tflite.tflite.Model
print(dir(tflite.tflite.Model))

# from tflite.tflite.Model import Model


# from tflite.BuiltinOperator import BuiltinOperator
# tflite = tflite.tflite
from tflite.tflite.Model import Model
print(dir(Model))
