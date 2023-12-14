# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
import random

dict1 = {

}

for i in range(1,6):
    r = random.randint(1,15)
    j = input("Enter Value:")
    dict1[r]=[j]
print(dict1)