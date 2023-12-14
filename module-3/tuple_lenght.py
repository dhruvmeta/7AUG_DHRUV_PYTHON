# Write a Python program to find the length of a tuple. 

list1= []
n = int(input("Enter no. of entries: "))
for i in range(n):
    i = input("Enter values as desire: ")
    list1.append(i)
    
tuple1 = (tuple(list1))
print(tuple1)
print(f"The lenght of Tuple is :",len(tuple1))