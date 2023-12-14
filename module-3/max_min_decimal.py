# Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers. 

print("Enter the Multiple Decimal Points Comma Separate...")
dec = []
for i in range(0,5):
    x = float(input("enter a decimal: "))
    dec.append(x)

print("Maximum: ", max(dec))
print("Minimum: ", min(dec))