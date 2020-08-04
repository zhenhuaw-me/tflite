import os
import tflite


def test_import():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    tflm_dir = os.path.abspath(cur_dir + '/../assets/tests')
    tflm_name = 'mobilenet_v2_1.0_224.tflite'
    path = os.path.join(tflm_dir, tflm_name)
    with open(path, 'rb') as f:
        buf = f.read()
        model = tflite.Model.GetRootAsModel(buf, 0)
    assert(model.Version() == 3)


if __name__ == '__main__':
    test_import()
