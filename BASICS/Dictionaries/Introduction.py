# Dictionary is an ordered collection of items.
# It stores data in the form of key-value pairs.

dic = {
    "Harry": "Human Being",
    "Spoon": "Object"
}


# 1. To print the dictionary

print(dic)


# 2. To access value using key

print(dic["Harry"])


# 3. Another way to access value

print(dic.get("Harry"))


# 4. If key does not exist

# print(dic["S"])
# This will throw KeyError


print(dic.get("S"))
# This will return None


# 5. To get all keys

print(dic.keys())

#6.To get all values

print(dic.values())


#6. Iteration on Dic

Student = {
    "name" : "Divyanshu Gupta",
    "Std" : "Btech",
    "UniversityRollNo" : 2300970310077
}

#Printing all the key names one by one

for x in Student:
    print(x)

#Printing all the Values names one by one

for x in Student:
    print(Student[x])

# to print both key and value we use items function

for x,y in Student.items():
    print(x,y)