
n = int (input("enter positive integer"))
a=0
b=1
c=a+b
i=1
print("fibonacci series is :")
while i<n:
    i+=1
    print(a)
    a=b
    b=c
    c=a+b
    