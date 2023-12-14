# Write a Python function that takes a list and returns a new list with unique elements of the first list.
import random

list1 = []

n=int(input("Enter number of elements:")) 

for i in range(n):
    i = input("Enter list elements:")
    if i not in list1:
        list1.append(i)
# relist1    

print(list1)