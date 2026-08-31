import numpy as np
import numpy as np

a = [[10, 20, 30, 40],
     [50, 60, 70, 80]]

arr = np.array(a)

print(arr)

print(arr.shape)      # rows, columns
print(len(arr))       # number of rows
print(np.size(arr))   # total number of elements
print(type(arr))      # type of variable/object
print(arr.ndim)       # number of dimensions
print(arr.dtype)      # data type of array elements