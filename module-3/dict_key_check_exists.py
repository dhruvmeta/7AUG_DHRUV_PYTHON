# Write a Python script to check if a given key already exists in a dictionary.

dic1={'ID':'101', 'sub':'python'}
i = input("Enter key:")

if i in dic1.keys():
    print("Alredy exists")
else:
    print("Does not exists")