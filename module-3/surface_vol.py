# Write a Python program to calculate surface volume and area of a cylinder 

import math

# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².

r = float(input("Enter raduis of cylinder: "))
h = float(input("Enter height of cylinder: "))

V = (math.pi)*(r*r*h)
a1 = ((math.pi)*(r*h))
a2 = ((math.pi)*(r*r))
a = 2*(a1) + 2*(a2)
print("The Surface volume of cylinder is: ", V)
print("The Area of cylinder is: ", a)