import numpy as np



# np.mean(a)    → Average
# np.median(a)  → Middle value
# np.std(a)     → Data kitna spread hai
# Mode          → Sabse zyada baar aane wali value
# np.var(a)     → Variance std ka sqaure

# Baked food prices
baked_food = [300, 150, 130, 200, 280, 170, 188, 200]

# Convert list into NumPy array
a = np.array(baked_food)

# 1. Mean
mean = np.mean(a)
print("Mean:", mean)

# 2. Median
median = np.median(a)
print("Median:", median)

# 3. Standard Deviation
std = np.std(a)
print("Standard Deviation:", std)

# 4. Mode
values, counts = np.unique(a, return_counts=True)
mode = values[np.argmax(counts)]
print("Mode:", mode)

# 5. Variance
variance = np.var(a)
print("Variance:", variance)

