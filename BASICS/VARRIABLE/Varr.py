# Python Variables

# Variable ek placeholder hota hai jo value ko store karta hai

name = "Divyanshu"
age = 21
student_name = "Divyanshu"
_marks = 85

print(name)
print(age)
print(student_name)
print(_marks)


# RULE 1: Python case-sensitive hoti hai
Name = "Rahul"

print(name)   # Divyanshu
print(Name)   # Rahul


# RULE 2: Variable name mein space nahi de sakte
# first name = "Divyanshu"   # Wrong

# Space ki jagah underscore (_) use karte hain
first_name = "Divyanshu"
print(first_name)


# RULE 3: Variable number se start nahi ho sakta
# 1name = "Divyanshu"        # Wrong

# Lekin number baad mein use kar sakte hain
name1 = "Divyanshu"
print(name1)


# RULE 4: Special characters use nahi kar sakte
# @name = "Divyanshu"        # Wrong
# first-name = "Divyanshu"   # Wrong

# Underscore (_) allowed hai
first_name = "Divyanshu"
print(first_name)


# RULE 5: Variable letter ya underscore se start hona chahiye
student = "Divyanshu"
_student = "Divyanshu"

print(student)
print(_student)