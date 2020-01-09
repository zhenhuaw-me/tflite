import os

HERE = os.path.abspath(os.path.dirname(__file__))

def getPath(key):
  root_dir = os.path.abspath(os.path.join(HERE, '..'))
  if key == 'root': return root_dir
  elif key == 'mobilenet': return os.path.join(root_dir, '3rdparty/mobilenet_v1_1.0_224_quant.tflite')
  else: raise ValueError("Unsupported path key: %s" % key)

