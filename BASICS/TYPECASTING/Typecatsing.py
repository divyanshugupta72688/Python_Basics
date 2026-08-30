# type catsing means conversion of data types of one data type into another data types

# there are two types of conversion

#1.implicit type conversion that convert datatypes automatic
a = 123
b = 123.25
print(type(a))
print(type(b))

c = a+b
print(c)
print(type(c))


# explicit type conversion we have to convert data types manual
d = "123"
print("before convesion :")
print(type(d))

d = int(d)
print("after convesion :")
print(type(d))