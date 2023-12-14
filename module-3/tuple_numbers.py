# Write a Python program to create a tuple with numbers. 

n = int(input("Enter no. of entries: "))
list1 = []



for i in range(n):
    i= input("Enter valid integer : ")
    if i.isnumeric():
        list1.append(i)
    else:
        pass
print(tuple(list1))