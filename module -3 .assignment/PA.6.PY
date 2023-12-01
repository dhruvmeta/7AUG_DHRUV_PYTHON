
list1=[]
n = int(input("enter the number :" )) #4
for i in range (n) :
    i = input("enter:")
    list1.append(i)
        
t=tuple(list1)
print("tuple:",t)

for i in range(len(t)):

    for j in range(i+1,len(t)):
        if t[i]==t[j]:
            print("tuple reapet :", t[i])