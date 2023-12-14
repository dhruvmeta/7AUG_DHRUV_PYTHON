# Write a Python program to replace last value of tuples in a list. 

list1 = [(1,2), (2,3), (3,4)]

x=(7,8)
print("List: ",list1)
list1.remove((3,4))
list1.append(x)
tuple1 = tuple(list1)
print("Tuple: ",tuple1)