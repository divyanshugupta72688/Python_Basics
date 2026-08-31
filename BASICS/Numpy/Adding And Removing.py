import numpy as np

# Add Element atwill index using insert function

arr = np.array([10, 20, 30, 40])
result = np.insert(arr, 2, 99)
print(result)


# add element using append function

result = np.append(arr,50)
print(result)

# delete element using delete at will index

result = np.delete(arr, 2)

print(result)