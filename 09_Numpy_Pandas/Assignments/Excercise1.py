# Create two-dimensional 3×3 array and perform ndim, shape, slicing operation on it.
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
print("Dimension of array:",arr_2d.ndim)
print("Shape of array:",arr_2d.shape)
print("Reshaped array:",arr_2d.reshape(3,3))
print("First row:", arr_2d[0])              
print("First column:", arr_2d[:, 0])        
print("Element at (2,2):", arr_2d[1, 1])    
print("Subarray (first 2 rows & cols):\n", arr_2d[0:2, 0:2])