# Function for user registration
def singin():
    name = input("Enter a name: ")
    id= int(input("Enter you id: "))
    #user_dic = {'user_name':name,'user_id':id}      
    #city=input("enter your city name:")
    
    with open("user_database.txt", "a") as file:
        file.write(f"{name}:{id}\n")
    print("singin successful!")

# Function for user login
def login():
    name = input("Enter your name: ")
    id = int(input("Enter your id: "))
    
    with open("user_database.txt", "r") as file:
        for line in file:
            stored_username, stored_id = line.strip().split(":")
            if name == stored_username and id == stored_id:
                print("Login successful!")
                return
    
            
print("Login failed. Check your username and id.")
    

# Main program loop
"""while True:
    print("1. singinr")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        singin()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")
"""
        
                     




