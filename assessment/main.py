from fruit_manager import manager_role

main_fruit_dic = {}

while True :

    print("welcome to your market !!!")
    print("  ")
    print("1)manager") 
    print("2)customer")
    print(" ")
    choice =int(input(" select your role : "))
    print(" ")

    if choice==1:
        manager_role()

    else:
        print("error")
print (input("enter y for yes and n for no :"))



                  

        