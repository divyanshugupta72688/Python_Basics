import numpy as np

arr = np.array([20,40,60,70])

# Sum

print(np.sum(arr))

# Max

print(np.max(arr))

# Min

print(np.min(arr))

# Mean

print(np.mean(arr))

#cumsum

print(np.cumsum(arr))

# cumprod

print(np.cumprod(arr))

# TWO-DIMENSIONAL DATA

a = [100,150,199,200,250,130]
b = [10,50,30,40,30,10]

price = np.array(a)
quantity = np.array(b)
print(price,"\n",quantity)


print()

c = (np.cumprod([price,quantity],axis=0))

print(c[1].sum())