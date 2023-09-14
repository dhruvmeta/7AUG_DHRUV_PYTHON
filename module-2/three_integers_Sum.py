# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.  

a = int(input("Enter A:")) 
b = int(input("Enter B:"))
c = int(input("Enter C:"))

if a==b or b==c or a==c:
    print("Sum is Zero!!!")
else:
    print("The sum of A + B + C = ", a+b+c)