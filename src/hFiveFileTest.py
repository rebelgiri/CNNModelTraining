import h5py
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import load_model

# my_array = np.fromfile('/home/giriraj/CNNClassifier/Example/ld-model-cnn-classifier-example/model/to-deploy'
#                      '/trained_model_2019-10-08 12-29-36.h5', dtype=float)
# f = h5py.File(
#    '/home/giriraj/CNNClassifier/Example/ld-model-cnn-classifier-example/model/to-deploy/trained_model_2019-10-08 '
#    '12-29-36.h5',
#    'r')

# print(f)

# for key in f.keys():
#    print(key)  # Names of the groups in HDF5 file.

# Get the HDF5 group
# group = f[key]

# Checkout what keys are inside that group.
# for key in group.keys():
#   print(key)


# After you are done
# f.close()


filename = '/home/giriraj/CNNClassifier/Example/ld-model-cnn-classifier-example/model/to-deploy/trained_model_2019-10' \
           '-02 18-12-20.h5'

# with h5py.File(filename, 'r') as f:
# List all groups
#   print("Keys: %s" % f.keys())
#  a_group_key = list(f.keys())[0]

# Get the data
# data = list(f[a_group_key])

# print(f.values())

f = h5py.File(filename, 'r')
print(list(f.keys()))
opt_weight = f['optimizer_weights']
model_weight = f['model_weights']
print(f['model_weights'])
print(f['optimizer_weights'])

print(opt_weight)
print(model_weight)

model = load_model(filename)
print(model.summary())