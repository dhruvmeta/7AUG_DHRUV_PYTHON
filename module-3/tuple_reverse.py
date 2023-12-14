#  Write a Python program to reverse a tuple. 


list1 = []

n = int(input("Enter number of inputs for list:"))
for i in range(n):
    i = input("Enter :")
    list1.append(i)
print("List:",list1)    

# tuple1 = (list1)
tuple1 = tuple(list1[::-1])
# tuple1 = list1[::-1]
print("Tuple reversed:",tuple1)