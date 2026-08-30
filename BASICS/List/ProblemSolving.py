A = ["Ross","Rachel","Monica","Joe"]

#Quetion1.WAP to swap first and fourth element

A[0],A[3] = A[3],A[0]
print(A)
#Quetion2.WAP to add a new value at second position

A.insert(1,"Surabhi")
print(A)

#Quetion3.WAP to delete a value from third position

A.pop(2)
print(A)

B = [13,7,12,10]

#Quetion4.WAP to multiply all the numbers in the list

mul = 1
for i in B :
    mul *= i
print(mul)

#Quetion5.WAP to get the largest number from the list

B.sort()
print(B[-1])

#Quetion6.WAP to get the smallest number from the list

print(B[0])