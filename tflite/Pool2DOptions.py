# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Pool2DOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Pool2DOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPool2DOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def Pool2DOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # Pool2DOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Pool2DOptions
    def Padding(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # Pool2DOptions
    def StrideW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool2DOptions
    def StrideH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool2DOptions
    def FilterWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool2DOptions
    def FilterHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Pool2DOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Pool2DOptionsStart(builder): builder.StartObject(6)
def Start(builder):
    return Pool2DOptionsStart(builder)
def Pool2DOptionsAddPadding(builder, padding): builder.PrependInt8Slot(0, padding, 0)
def AddPadding(builder, padding):
    return Pool2DOptionsAddPadding(builder, padding)
def Pool2DOptionsAddStrideW(builder, strideW): builder.PrependInt32Slot(1, strideW, 0)
def AddStrideW(builder, strideW):
    return Pool2DOptionsAddStrideW(builder, strideW)
def Pool2DOptionsAddStrideH(builder, strideH): builder.PrependInt32Slot(2, strideH, 0)
def AddStrideH(builder, strideH):
    return Pool2DOptionsAddStrideH(builder, strideH)
def Pool2DOptionsAddFilterWidth(builder, filterWidth): builder.PrependInt32Slot(3, filterWidth, 0)
def AddFilterWidth(builder, filterWidth):
    return Pool2DOptionsAddFilterWidth(builder, filterWidth)
def Pool2DOptionsAddFilterHeight(builder, filterHeight): builder.PrependInt32Slot(4, filterHeight, 0)
def AddFilterHeight(builder, filterHeight):
    return Pool2DOptionsAddFilterHeight(builder, filterHeight)
def Pool2DOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(5, fusedActivationFunction, 0)
def AddFusedActivationFunction(builder, fusedActivationFunction):
    return Pool2DOptionsAddFusedActivationFunction(builder, fusedActivationFunction)
def Pool2DOptionsEnd(builder): return builder.EndObject()
def End(builder):
    return Pool2DOptionsEnd(builder)