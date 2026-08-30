#1.WAP TO SORT A DICTIONARY BY VALUE
a = {
    "a":12,

    "c": 6,
    "b": 23,
    "e": 45,
    "d": 91,
}
a = sorted(a.values())
print(a)






#2.WAP TO MULTIPLY ALL THE ITEMS IN A DICTIONARY
mul = 1
for i in a.values():
    mul *= i
print(mul)

#3.WAP TO SORT A DICTIONARY BY KEY

a = sorted(a.keys())
print(a)