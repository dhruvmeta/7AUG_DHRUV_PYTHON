# Write a Python function that takes two lists and returns true if they have
# at least one common member

l1 = [1, 2, 4, 5, 7, 6]
l2 = [22, 3, 5, 7, 11]

# print(list(set(l1).intersection(l2)))
common_list=[]
for elements in l1:
    if elements in l2:
        # print("True")
        common_list.append(elements)

print(common_list)