# Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle

class rectangle():
    def area(self):
        self.lenght = float(input("Enter lenght of rectangle: ")) 
        self.breath = float(input("Enter breath of rectangle: ")) 
        self.area = self.lenght*self.breath 
        print(self.area)
a = rectangle()
a.area()