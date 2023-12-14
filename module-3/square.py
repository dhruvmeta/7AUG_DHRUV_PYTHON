# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30. 

l1 = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13,14 ,15, 16, 17, 18, 19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

sq_list = []
v = []
for elements in range(1,6):
    elements*= elements
    sq_list.append(elements)

for e in range(26,31):
    e*=e
    v.append(e)



print(sq_list+v)