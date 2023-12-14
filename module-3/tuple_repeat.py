# Write a Python program to find the repeated items of a tuple. 

list1 = []

n = int(input("Enter number of inputs for list:"))
for i in range(n):
    i = input("Enter :")
    list1.append(i)
# print("List:",list1)
tuple1 = tuple(list1)
print("Tuple:", tuple1)

for i in range(len(tuple1)):
 
    for j in range(i+1,len(tuple1)):
 
        if tuple1[i]==tuple1[j]:
 
            print("The repeated member of tuple:",tuple1[i])