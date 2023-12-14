# Write a Python program to remove an empty tuple(s) from a list of tuples. 

t = ('abhi', '', 'karan', '', 'surya', 'man')

l = []

for i in t:
    l.append(i)
    if(len(i) == 0):
        l.remove(i)    
        t = tuple(l)
        print(t)