# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LogSoftmaxOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LogSoftmaxOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsLogSoftmaxOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def LogSoftmaxOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LogSoftmaxOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def LogSoftmaxOptionsStart(builder):
    builder.StartObject(0)

def Start(builder):
    LogSoftmaxOptionsStart(builder)

def LogSoftmaxOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return LogSoftmaxOptionsEnd(builder)
