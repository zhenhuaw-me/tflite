# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StableHLOCompositeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StableHLOCompositeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStableHLOCompositeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def StableHLOCompositeOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # StableHLOCompositeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StableHLOCompositeOptions
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # StableHLOCompositeOptions
    def DecompositionSubgraphIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StableHLOCompositeOptions
    def CompositeAttributes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # StableHLOCompositeOptions
    def CompositeAttributesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # StableHLOCompositeOptions
    def CompositeAttributesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StableHLOCompositeOptions
    def CompositeAttributesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # StableHLOCompositeOptions
    def CompositeAttributesFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # StableHLOCompositeOptions
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def StableHLOCompositeOptionsStart(builder):
    builder.StartObject(5)

def Start(builder):
    StableHLOCompositeOptionsStart(builder)

def StableHLOCompositeOptionsAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    StableHLOCompositeOptionsAddName(builder, name)

def StableHLOCompositeOptionsAddDecompositionSubgraphIndex(builder, decompositionSubgraphIndex):
    builder.PrependInt32Slot(1, decompositionSubgraphIndex, 0)

def AddDecompositionSubgraphIndex(builder, decompositionSubgraphIndex):
    StableHLOCompositeOptionsAddDecompositionSubgraphIndex(builder, decompositionSubgraphIndex)

def StableHLOCompositeOptionsAddCompositeAttributes(builder, compositeAttributes):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(compositeAttributes), 0)

def AddCompositeAttributes(builder, compositeAttributes):
    StableHLOCompositeOptionsAddCompositeAttributes(builder, compositeAttributes)

def StableHLOCompositeOptionsStartCompositeAttributesVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartCompositeAttributesVector(builder, numElems):
    return StableHLOCompositeOptionsStartCompositeAttributesVector(builder, numElems)

def StableHLOCompositeOptionsAddCompositeAttributesFormat(builder, compositeAttributesFormat):
    builder.PrependInt8Slot(3, compositeAttributesFormat, 0)

def AddCompositeAttributesFormat(builder, compositeAttributesFormat):
    StableHLOCompositeOptionsAddCompositeAttributesFormat(builder, compositeAttributesFormat)

def StableHLOCompositeOptionsAddVersion(builder, version):
    builder.PrependInt32Slot(4, version, 0)

def AddVersion(builder, version):
    StableHLOCompositeOptionsAddVersion(builder, version)

def StableHLOCompositeOptionsEnd(builder):
    return builder.EndObject()

def End(builder):
    return StableHLOCompositeOptionsEnd(builder)
