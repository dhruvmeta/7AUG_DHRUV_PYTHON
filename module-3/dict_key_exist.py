#  Write a Python script to check if a given key already exists in a dictionary.

dic1={'ID':'101', 'sub':'python', 'city':'rajkot', 'centre':'Gujarat'}

key = input("Enter the key: ")
value = input("Enter Value: ")

if key in dic1.keys():
    print("Key already Exists...")   
else:
    dic1[key]=[value]
    print(dic1)