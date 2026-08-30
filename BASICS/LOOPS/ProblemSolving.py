print("Welcome to the Loops Problem Solving Program")


# Quetion1.write a program to find a sum of all the even numbers up to 50

sum = 0
for i in range(0,51):
    if i % 2 == 0:
        sum = sum + i


print(sum)

# Quetion2.WAP to write first 20 Numbers and thier squared number

for i in range(1,21):
    print(i,i*i)

# Quetion3.WAP to find sum of first 10 odd numbers using while loop

summ = 0
n = 0

while n <= 20:
    if n % 2 != 0:
        summ = summ + n
    n = n + 1

print(summ)


# Quetion4.WAP to check a number is divisival by 8 and 10 upto 100 numbers

for i in range(1,100):
    if i % 8 == 0 and i % 12 == 0:
        print(i)


# Quetion5.WAP To create a billing system at supermarket

while True :
    name = input("Enter a CustomerName: ")
    total = 0

    while True:
        print("Enter the amount and quantity")
        amount = float(input("Enter the amount: "))
        quantity = int(input("Enter the quantity: "))
        total = total + amount*quantity
        repeat = input("Would you like to continue? (y/n): ")
        if repeat == "N" or repeat == "n":
            break
    print("-"*40)
    print("Name : ",name)
    print("Amount to be paid : ",total)
    print("-" * 40)
    print("-------Happy Shopping------")

    repeat1 = input("Would you like to continue? (y/n): ")
    if repeat1 == "N" or repeat1 == "n":
        break