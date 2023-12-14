# Write a Python program to create a tuple with different data types. 

list1= []
n = int(input("Enter no. of entries: "))
for i in range(n):
    i = input("Enter values as desire: ")
    list1.append(i)
    
print(tuple(list1))

for t in list1:
    tuple1 = tuple(list1)