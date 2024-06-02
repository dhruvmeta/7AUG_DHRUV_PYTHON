# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle 
import math
class circle():
    rad = float(input("Enter radius of circle: "))

    def area(self):
        area = math.pi*(self.rad)*(self.rad)
        print(f"Area of circle with radius {self.rad} is :", area)

    def perimeter(self):
        per = (math.pi*(self.rad))
        print(f"The perimeter of circle with radius {self.rad} is : ", 2*per)
    
c = circle()
c.area()
c.perimeter()