# Tuple is an ordered and immutable collection of elements

a = ("Hulk", "Thor", "IronMan", "Captain America", "Hulk")


# 1. To find the length of a tuple

print(len(a))
# Output: 5


# 2. To count the occurrence of a particular element

print(a.count("Hulk"))
# Output: 2


# 3. To find the index of an element

print(a.index("IronMan"))
# Output: 2


# 4. To access an element using index

print(a[0])
# Output: Hulk


# 5. Negative indexing

print(a[-1])
# Output: Hulk


# 6. Tuple slicing

print(a[0:3])
# Output: ('Hulk', 'Thor', 'IronMan')


# 7. Reverse tuple using slicing

b = (a[::-1])
print(b)
print(a)









