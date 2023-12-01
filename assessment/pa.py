list1 = [(1,2,33), (22,43,521), (21,3424,112)]
word = (16,6,2003)

print("list:", list1)

list1.remove((21,3424,112))
list1.append(word)
t1= tuple(list1)
print("Tuple:",t1)