# Write a Python program to check whether a list contains a sub list 

list1 = ['apple','Tomato', 5, 8, 9]
sub_list = [5,9]

print("Given list ",list1)
print("Given sub list",sub_list)

if (set(sub_list).intersection(set(list1))):
   print(f"Sub list is part of {list1}")
else:
   print(f"Sub list is not part of  {list1}")