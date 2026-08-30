#1. Write a function to find maximum of three numbers in python

def Maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print(Maximum(2,5,4))

#2.Write a function to create and print a list where the values are sqaure
# of numbers between 1 and 30

def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())


#3.Write a function that takes a number as a parameter and check if number is prime or not

def CheckPrimeOrNot(x):
    if x == 1:
        print("Not Prime")

    elif x == 2:
        print("Prime")

    elif x > 2:
        for i in range(2, x):
            if x % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")


CheckPrimeOrNot(15)
