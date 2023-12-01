"""Write a Python function to get the largest number, smallest num and sum 
of all from a list. """

n = int(input("Enter no. of values for list: "))
l=[]
for i in range(n):
    a = int(input("Enter values:"))
    l.append(a)
print(l)

def largest_smallest_sum():

    print(f"largest number of the list{list1}:",max(list1))
    print(f"smallest number of the list{l2}:",min(l2))
    print(f"sum number of the list{l3}:",sum(l3))

largest_smallest_sum()