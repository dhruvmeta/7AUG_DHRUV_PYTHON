# Write a Python program to convert a list to a tuple.


list1 = []

n = int(input("Enter number of inputs for list:"))
for i in range(n):
    i = input("Enter :")
    list1.append(i)
print("List:",list1)    
    
tuple1 = tuple(list1)
print("Tuple:",tuple1)