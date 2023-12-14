# Write a Python program to find the highest 3 values in a dictionary
from collections import Counter
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}

k = Counter(my_dict)
 
# Finding 3 highest values
h = k.most_common(3) 
 
print("Dictionary with 3 highest values:")
 
for i in h:
    print(i[0],":",i[1],"")