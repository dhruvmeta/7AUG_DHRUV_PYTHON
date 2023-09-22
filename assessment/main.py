from fruit_manager import manager_role

Y_or_N='Y'

while Y_or_N!='N':

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



    Y_or_N = input("Do  you want to  perform more operation : press y for yes and n for no : ").capitalize()




                  

        