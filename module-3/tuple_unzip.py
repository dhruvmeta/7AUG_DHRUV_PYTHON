#  Write a Python program to unzip a list of tuples into individual lists. 
list1 = [('have', 11), ('a', 42), ('good', 23), ('day', 94)] 

a = []
b = []
for i in list1:
    a.append(i[0])
    b.append(i[1])
print((a,b))