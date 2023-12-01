from auth_system import singin
from auth_system import login



while True:

    print("1. singing")
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
        
  