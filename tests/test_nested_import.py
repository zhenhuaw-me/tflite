from tflite.tflite.Model import Model
import util_for_test

def read_model(key: str):
    with open(util_for_test.getPath(key), 'rb') as f:
        buf = f.read()
        model = Model.GetRootAsModel(buf, 0)
    return model

assert(read_model('mobilenet').Version() == 3)
assert(read_model('mobilenet_quant').Version() == 3)
