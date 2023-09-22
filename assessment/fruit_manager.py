def manager_role():
    print("")
    print("             Fruit Market Manager")
    print("")
    print("             1)Add fruit stock")
    print("             2)View fruit stock")
    print("             3)update fruite stock")
    print("")   

    choice_manager =int(input("enter your choice:"))
  

    
    if choice_manager ==1:
            print("add fruit stock:")
            fruit_name=input("enter your fruit name :")
            fruit_qty=int(input("Enter fruit qty :"))
            fruit_price=int(input("enter fruit price :"))
            fruit_dic = {fruit_name:{'qty':fruit_qty, 'price':fruit_price}}      
            print(fruit_dic)

            with open('Fruit_stock.txt', 'a') as file:
                file.write(f"{fruit_dic} ||")


    elif choice_manager==2:
            
        with open("Fruit_stock.txt", 'r') as f:
            print(f.readline())

    else:
        print("error")
        
         

