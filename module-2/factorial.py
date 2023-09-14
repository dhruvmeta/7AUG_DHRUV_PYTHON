
n= int(input("enter positev integer:"))
factorial = 1

if n<0:
    print("wronge input")
elif n==0:
    print  ("factorial of 0 is 1!!")
else:
    for i in range (1,n+1):
        factorial*= i
    print(f"the fatorial value of {n} is {factorial}!!")