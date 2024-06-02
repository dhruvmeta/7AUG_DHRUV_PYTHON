# Write a Python program to copy the contents of a file to another file. 

with open('globalwarming.txt', 'r') as f:
    line= f.read()

with open("Copy.txt", 'w') as f2:
    f2.write(line)a