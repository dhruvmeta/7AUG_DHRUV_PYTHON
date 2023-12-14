# Write a Python program to calculate the area of a trapezoid 

# forumla  A=((a+b)/2)*h

#           ____b1_____
    #     /            \ 
    #    /              \h
    #   /_______b2_______\
    
base_1 = float(input('Please Enter the First Base of a Trapezoid: '))
base_2 = float(input('Please Enter the Second Base of a Trapezoid: '))
height = height = float(input('Please Enter the Height of a Trapezoid: '))

area = ((base_1+base_2)/2)*height

print(f"Area of trapeziod is: {area} ")