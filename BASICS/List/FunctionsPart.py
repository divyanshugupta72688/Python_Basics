a = ["Hulk", "Thor", "IronMan", "Captain America"]


# 1. To find the length of a list

print(len(a))
# Output: 4


# 2. To count the occurrence of a particular element

print(a.count("Hulk"))
# Output: 1


# 3. To add an element at the end of the list

a.append("SpiderMan")
print(a)
# ['Hulk', 'Thor', 'IronMan', 'Captain America', 'SpiderMan']


# 4. To add an element at a specific location

a.insert(1, "Vision")
print(a)
# ['Hulk', 'Vision', 'Thor', 'IronMan', 'Captain America', 'SpiderMan']


# 5. To remove a particular element

a.remove("Hulk")
print(a)
# ['Vision', 'Thor', 'IronMan', 'Captain America', 'SpiderMan']


# 6. To remove an element from a specific index

a.pop(2)
print(a)
# ['Vision', 'Thor', 'Captain America', 'SpiderMan']


#7.to create a copy of a list

b = a.copy()
print(b)
#['Hulk', 'Thor', 'IronMan', 'Captain America']


#8.to reverse the list

a.reverse()
print(a)
#['Captain America', 'IronMan', 'Thor', 'Hulk']

#9.to Sort the list

a.sort()
print(a)
#['Captain America', 'Hulk', 'IronMan', 'Thor']

#10.to clear all the data from the list

a.clear()
print(a)
# it gives the empty list[]