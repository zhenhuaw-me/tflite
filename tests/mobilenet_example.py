import tflite
import util_for_test

# Example of parsing a TFLite model with `tflite` python package.
# Use this package, you can *import* the `tflite* package ONLY ONCE.
# Otherwise, you need to import every class when using them.

def read_model(key: str):
    with open(util_for_test.getPath(key), 'rb') as f:
        buf = f.read()
        model = tflite.Model.GetRootAsModel(buf, 0)
    return model


############# model #########################################################

model = read_model('mobilenet')

# Version of the TFLite Converter.
assert(model.Version() == 3)

# Strings are binary format, need to decode.
# Description is useful when exchanging models.
assert(model.Description().decode('utf-8') == 'TOCO Converted.')

# How many operator types in this model.
assert(model.OperatorCodesLength() == 5)

# A model may have multiple subgraphs.
assert(model.SubgraphsLength() == 1)

# How many tensor buffer.
assert(model.BuffersLength() == 90)


############# subgraph ######################################################

# Chose one subgraph.
graph = model.Subgraphs(0)

# Tensors in the subgraph are represented by index description.
assert(graph.InputsLength() == 1)
assert(graph.OutputsLength() == 1)
assert(graph.InputsAsNumpy()[0] == 88)
assert(graph.OutputsAsNumpy()[0] == 87)
# All arrays can dump as Numpy array, or access individually.
assert(graph.Inputs(0) == 88)
assert(graph.Outputs(0) == 87)

# Name may used to debug or check for model containing multiple subgraphs.
assert(graph.Name() == None)

# Operators in the subgraph.
assert(graph.OperatorsLength() == 31)

# Let's use the first operator.
op = graph.Operators(0)


############# operator type #################################################

# Operator Type is also stored as index, which can obtain from `Model` object.
op_code = model.OperatorCodes(op.OpcodeIndex())

# The first operator is a convolution.
assert(op_code.BuiltinCode() == tflite.BuiltinOperator.CONV_2D)

# Custom operator need more interface, won't cover here.
assert(op_code.BuiltinCode() != tflite.BuiltinOperator.CUSTOM)


############# the operator ##################################################

# The first operator is a convolution.

# The inputs are: data, weight and bias.
assert(op.InputsLength() == 3)
assert(op.OutputsLength() == 1)

# The data of first Conv2D is input of the model
assert(op.Inputs(0) == 88)
assert(op.Inputs(0) == graph.Inputs(0))

# Operators have dedicated options per its type
assert(op.BuiltinOptionsType() == tflite.BuiltinOptions.Conv2DOptions)
op_opt = op.BuiltinOptions()


############# operator option ###############################################

# Check the Conv2D options.

# Parse the Table of options.
opt = tflite.Conv2DOptions()
opt.Init(op_opt.Bytes, op_opt.Pos)

# The options.
assert(opt.Padding() == tflite.Padding.SAME)
assert(opt.StrideW() == 2)
assert(opt.StrideH() == 2)
assert(opt.DilationWFactor() == 1)
assert(opt.DilationHFactor() == 1)

# Further check activation function type if there were.
assert(opt.FusedActivationFunction() == tflite.ActivationFunctionType.NONE)


############# tensor ########################################################

# Check the weight tensor of the first convolution.
tensor_index = op.Inputs(1)

# use `graph.Tensors(index)` to get the tensor object.
tensor = graph.Tensors(tensor_index)

# view the shape
assert(tensor.ShapeLength() == 4)
assert(tensor.ShapeAsNumpy()[1] == 3)
# All arrays can dump as Numpy array, or access individually.
assert(tensor.Shape(1) == 3)

# data type has been encoded
assert(tensor.Type() == tflite.TensorType.UINT8)

# name is in binary format, decode it
assert(tensor.Name().decode('utf-8') ==
       'MobilenetV1/MobilenetV1/Conv2d_0/weights_quant/FakeQuantWithMinMaxVars')

# buffer of the tensor is represented in index too.
assert(tensor.Buffer() == 66)

# quantization parameters of the tensor, only valid for quantized model
assert(tensor.Quantization())

assert(not tensor.IsVariable())


############# quant #######################################################

# Quantization parameters of the tensor, only valid for quantized model
quant = tensor.Quantization()

# Scale and zero point
assert(quant.ScaleAsNumpy()[0] == 0.02182667888700962)
assert(quant.ZeroPointAsNumpy()[0] == 151)

# Min/max also avaiable
assert(quant.MinAsNumpy()[0] == -3.265998125076294)
assert(quant.MaxAsNumpy()[0] == 2.2779781818389893)

# All arrays can dump as Numpy array, or access individually.
assert(quant.Scale(0) == 0.02182667888700962)
assert(quant.ZeroPoint(0) == 151)
assert(quant.Min(0) == -3.265998125076294)
assert(quant.Max(0) == 2.2779781818389893)


############# memory #######################################################

# Get the buffer object.
buf = model.Buffers(tensor.Buffer())

assert(buf.DataLength() == 864)
assert(buf.DataAsNumpy()[0] == 151)
# All arrays can dump as Numpy array, or access individually.
assert(buf.Data(0) == 151)

# The Numpy array is flattened.
npa = buf.DataAsNumpy()
assert(npa.shape == (864,))
