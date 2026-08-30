# Tuple is an ordered and immutable collection of elements

a = ("apple", "banana", "grapes")

print(a)
print(type(a))


# Parentheses () are optional

b = "apple", "banana", "grapes"

print(b)
print(type(b))


# If you have a single element in a tuple,
# you must use a comma

c = ("apple",)

print(c)
print(type(c))


# Without comma, it is a string

d = ("apple")

print(d)
print(type(d))


# we can add element using list

a = list(a)
print(type(a))
a.append("Mango")
print(a)
a= tuple(a)
print(a)
print(type(a))