# Write a Python program to split a list into different variables. 

list1 = ['a', 'b', 'h', 'i']
str1 = ""
for i in list1:
   v = i
   v = input(f"Enter value of variable of {i}:")
   print(f"{i}=",v)