# Write a Python program to count the number of lines in a text file. 

with open('globalwarming.txt', 'r') as f:
    line= len(f.readlines())
print(line)