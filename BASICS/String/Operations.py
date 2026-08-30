a = "Hello World!"

# to find length of a string
print(len(a))

#to find the number of times a character is occuring
print(a.count("l"))

#convert each letter in string into UpperCase
print(a.upper())

#convert each letter in string into LowerrCase
print(a.lower())

# find out the index of letter in string
print(a.index("o"))

# we can also provide range to find out the index of letter in String
print(a.index("l",5,10))

#it is used to capatilize first letter of string
print(a.capitalize())

#to find the index number of a character
print(a.find("o"))

# strip()- Returns a trimmed version of A String

b = "     *******Harry Potter ............"
print(b.strip("*,., "))


# Splits the string at the specified seperator , returns a list

c = "#OOFD#OMW"
print(c.split("#"))
print(c.split(","))

#String Slicing

d = "Harry Potter and the Goblet of fire"
print(d[0:5])
print(d[-4:])

# to reverse a string in python
print(d[::-1])