#  Write a Python program to get unique values from a list 

list1 = []

n = int(input("Enter no. of elements to be:"))

for i in range(n):
    x = input("Enter unique values:") 
    list1.append(x)

print(set(list1))