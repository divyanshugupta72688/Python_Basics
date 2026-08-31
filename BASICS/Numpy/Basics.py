import numpy as np

a = np.array([1, 2, 3, 4])

print(a)
print(type(a))

# SLICING
# First element included and last element excluded
print(a[1:4])

# REVERSE AN ARRAY USING SLICING
print(a[::-1])


arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr)

print(arr[0:2, 0:2])   # slicing

print(arr[::-1, ::-1]) # reverse rows + columns

# ATTRIBUTES OF NUMPY

print(len(arr))
print(np.shape(arr))   # shape
print(np.size(arr))    # total number of elements
print(np.ndim(arr))    # number of dimensions
print(arr.dtype)       # data type