# Write a Python program to map two lists into a dictionary

l1 = ['a', 'b', 'c', 'd', 'e']
l2 = [1,2,3,4,5]

dic1 = {}
dic1= dict(zip(l1,l2))

print(dic1)