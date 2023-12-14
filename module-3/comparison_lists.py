# • How will you compare two lists?
"""sort() method or the sorted() function with the == operator
set() function with the == operator

Using the sort() Method or the sorted() Function to Compare Lists
You can use the sort() method or the sorted() function to sort lists with the purpose of comparing them for equality. The sort() method sorts the list in place, while the sorted() function returns a new list. After sorting, lists that are equal will have the same items in the same index positions. The == operator compares the lists, item by item (element-wise comparison).
The order of the original list items is not important, because the lists are sorted before comparison.
"""

# +++++++++++++++++++++ sort function

l1 = [1, 21 ,33, 5 ,9, 22]
l2 = [1, 241 ,313, 112, 22, 9]
l3 = [1, 21 ,33, 5, 22, 9]

l1.sort()
l2.sort()
l3.sort()

if l1 == l2:
    print("List l1 and l2 are same...")
elif l2 == l3:
    print("List l2 and l3 are same...")
elif l3 == l1:
    print("List l1 and l3 are same...")
else:
    print("All the lists are differnt...")


# +++++++++++++++++++++ sorted function


l1 = [10, 20, 30, 40, 50]
l2 = [20, 30, 50, 40, 70]
l3 = [50, 10, 30, 20, 40]

l1_sorted = sorted(l1)
l2_sorted = sorted(l2)
l3_sorted = sorted(l3)

if l1_sorted == l2_sorted:
    print ("The lists l1 and l2 are the same")
else:
    print ("The lists l1 and l2 are not the same")

if l1_sorted == l3_sorted:
    print ("The lists l1 and l3 are the same")
else:
    print ("The lists l1 and l3 are not the same")