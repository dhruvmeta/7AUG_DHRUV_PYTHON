# Write a Python program to read a file line by line and store it into a list


with open('globalwarming.txt', 'r') as f:
    line= f.readline()

print(line)

# remove new line characters
list1 = [x.strip() for x in line]
print(list1)