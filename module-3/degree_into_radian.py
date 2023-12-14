# Write a Python program to convert degree to radian
import math

# formula =  1Deg × π/180 = 0.01745Rad
degree = int(input("Enter degrees: "))

i = degree*((math.pi)/180)

print(f"Degree To radians: {i}")