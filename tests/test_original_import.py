import logging
import shrub
from tflite.Model import Model

def test_import():
    path = shrub.testing.download('mobilenet_v2_1.0_224.tflite')
    with open(path, 'rb') as f:
        buf = f.read()
        model = Model.GetRootAsModel(buf, 0)
    assert(model.Version() == 3)

if __name__ == '__main__':
    test_import()
