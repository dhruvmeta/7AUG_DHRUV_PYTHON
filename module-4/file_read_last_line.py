# Write a Python program to read last n lines of a file. 


with open('globalwarming.txt', 'r') as f:
    # print(f.readline()[-1:])
    for line in (f.readlines() [-1:]):
            print(line, end ='')