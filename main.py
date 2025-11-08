import auth
import mastersetup
from menuoptions import add_password, view_passwords

def start():
    auth.master_password_authentication()

def mainn():
    
    cipher = auth.master_password_authentication()

    if not cipher:
        return
    
    while True:
        print("\nPassword manager")
        print("1. Add a new password")
        print("2. View Saved Passwords")
        print("3. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1': 
            add_password(cipher)
        
        elif choice == '2':
            view_passwords(cipher)
            
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
    
        
if __name__ == "__main__":
    mainn()