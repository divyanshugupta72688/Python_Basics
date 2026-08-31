import numpy as np

arr1= np.array([30,40,50,60])
arr2 = np.array([70,80,90,100])

# ADDITION

print(arr1+arr2)# Operation
print(np.add(arr1,arr2))# function

# SUBSTRACTION

print(arr1-arr2)
print(np.subtract(arr1,arr2))

#MULTIPLICATION

print(arr1*arr2)
print(np.multiply(arr1,arr2))

#DIVISION

print(arr1/arr2)
print(np.divide(arr1,arr2))

#POWER

arr3 = np.array([3,4,2,1])
arr4 = np.array([2])
print(np.power(arr3,arr4))


# SQAURE ROOT

arr5 = np.array([9,16,4,1])
print(np.sqrt(arr5))