# Student = {
#     "name" : "Divyanshu Gupta",
#     "Std" : "Btech",
#     "UniversityRollNo" : 2300970310077
# }
#
# #1.get
#
# print(Student.get("Std"))
#
# #2.item
#
# print(Student.items())
#
# #3.keys
#
# print(Student.keys())
#
# #4.values
#
# print(Student.values())
#
# #5.copy
#
# d = Student.copy()
# print(d)
#
# #6.setdefault
#
# x = Student.setdefault("name","Ayush Gupta")
# print(x)
#
# #7.clear
#
# Student.clear()
# print(Student)

# Nested Dictionary

Employees = {
    1:{"name":"Divyanshu Gupta","Std":"Btech","gender":"Male"},
    2:{"name":"param Singh","Std":"Btech","age":24},
}

print(Employees)
print(Employees[1])
print(Employees[2]["name"])