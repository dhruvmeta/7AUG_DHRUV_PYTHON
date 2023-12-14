# Write a Python program to check multiple keys exists in a dictionary

dic1={'ID':'101', 'sub':'python', 'city':'rajkot', 'centre':'Gujarat'}

for key in dic1:
    key1 = input("enter key to find in keyword 1:")
    key2 = input("enter key to find in keyword 2:")

    print(dic1.keys() >= {key1} or {key2})

    # while key in dic1.keys():
    if key1 and key2 in dic1.keys():
        print("both are present")
    elif key1 or key2 in dic1.keys():
        print("either one is present")
    else:
        print("none is present")
    break