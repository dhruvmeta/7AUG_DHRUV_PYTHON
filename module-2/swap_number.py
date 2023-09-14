
a = int(input("Enter A:")) 
b = int(input("Enter B:"))
c = a 
a = b
b = c 

print("Swapped A:",a) 
print("Swapped B:",b)

#=================== without temp vairable
a = int(input("Enter A:"))
b = int(input("Enter B:"))

a, b = b, a

print("Swapped A:",a) 
print("Swapped B:",b)  