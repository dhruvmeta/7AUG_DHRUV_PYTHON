str = input("Enter gibberish:")

if len(str)%4==0:
    print(str[::-1])
else:
    print("not a muliple of 4")
    