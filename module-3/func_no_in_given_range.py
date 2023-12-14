# Write a Python function to check whether a number is in a given range

def range():
    n = int(input("enter the number in range 1 to 10:"))
    if n >=10 or n<=1:
        print("not in valid range")
    else:
        print(f"the input {n} is in valid range")
range()