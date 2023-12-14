# Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {1: 'two', 2: 'three', 3:'one'}
 

print("the Decending order:")
for w in sorted(my_dict, key = my_dict.get):
    print(w, my_dict[w])

print("")

print("the Ascending order:") 
for w in sorted(my_dict, key=my_dict.get, reverse=True):
    print(w, my_dict[w])