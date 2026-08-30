# List are the collection of ordered and mutable (it can be changed)
# Multiple datatypes can be written inside a list

fruits = ["apple", "banana", "cherry", 12, 14]

print(fruits)
print(type(fruits))

# Access last element
print(fruits[-1])

# List slicing
# Multiple elements can be accessed
print(fruits[0:2])

# Reverse the list
print(fruits[::-1])


# List Iteration

a = ["Hulk", "Thor", "IronMan", "Captain America"]


# 1. Iteration using for loop

for i in a:
    print(i)


# 2. Iteration using for loop with range and len()

for i in range(len(a)):
    print(a[i])


# 3. Iteration using while loop

i = 0

while i < len(a):
    print(a[i])
    i += 1


# 4. Iteration using Short-hand for loop

[print(i) for i in a]