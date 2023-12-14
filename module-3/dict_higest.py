# Write a Python program to find the highest 3 values in a dictionary

my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}
x = []
for i in my_dict.values():
    x.append(i)
    x.sort()
    x.reverse()
print(x)
print(x[:3])