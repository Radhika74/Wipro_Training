# Create one-dimensional array and perform ndim, shape, reshape operation on it.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print("Dimension of array:",arr.ndim)
print("Shape of array:",arr.shape)
print("Reshaped array:",arr.reshape(2,5))