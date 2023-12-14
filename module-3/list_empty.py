# Write a Python program to check a list is empty or not

list1 = [1, 3, 5, 5, 6]

for i in list1:
    print(i)
list1.clear()
if len(list1)==0:
    print("list is empty...")
else:
    print("list is not empty...")