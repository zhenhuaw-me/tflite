import os
import tflite


def test_opcode2name():
    assert(tflite.opcode2name(0) == 'ADD')


if __name__ == '__main__':
    test_opcode2name()
