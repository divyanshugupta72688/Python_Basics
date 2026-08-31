import numpy as np

arr1 = np.array([10,40,50])
arr2 = np.array([20,30,60])
print(np.concatenate([arr1,arr2]))


# concat the array using axis axis = 0 (vertical)
arr3 = np.array([[10, 40] ,[50,60]])
arr4 = np.array([[20, 30],[60,70]])
print(np.concatenate([arr3, arr4],axis=0))

print(np.concatenate([arr3, arr4],axis=1))



# to split a array

arr = np.array([10,20,30,40,50,60,70])
result = np.array_split(arr, 3)
print(result)
print(result[0])