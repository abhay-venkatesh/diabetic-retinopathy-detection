import sys
caffe_root = "../caffe/python/"
sys.path.insert(0, caffe_root)

from caffe.proto import caffe_pb2
import numpy as np

def mean_blobproto_to_array(blob):
    return np.array(blob.data).reshape(
        blob.channels, blob.height, blob.width)

in_file = sys.argv[1]
out_file = sys.argv[2]

data = open(in_file, "rb").read()
blob = caffe_pb2.BlobProto()
blob.ParseFromString(data)

nparray = mean_blobproto_to_array(blob)
r = nparray.mean(axis=(1,2))
print(list(r))
f = file(out_file, "wb")
np.save(f, nparray)
f.close()
