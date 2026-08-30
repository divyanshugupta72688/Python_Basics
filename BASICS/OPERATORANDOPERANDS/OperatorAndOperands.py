#exponantional operaror
a = 2**5
print(a)
# floor division
b=8//3
print(b)

# LOGICAL OPERATOR->

#1.OR OPERARATOR

print(3>7 or 4>1)

#2.and operator
print(3>7 and 4>1)

#3.NOT OPERATOR

print(not (3>7 or 4>1))

#identity OPERATOR->
# check karta hai memory me jha save hai vo equal hai ki nahi

# two types of identity operator

#1.is and 2. is not

c = 123
d="123"
print(c is d)

print(c is not d)


# MEMBERSHIP OPERATOR TWO TYPE - IN OR NOT IN

g = "hello"
print("e" not in g)
print("e"  in g)


marks = 45

if marks >= 90:
    print("you can go for a trip")
elif marks >= 80 and marks < 90:
    print("you will get  a new  phone")
elif marks >= 70 and marks < 80:
    print("you will get  a new  book")
else:
    print("you will not get your phone back ")