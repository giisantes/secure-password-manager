import auth
import mastersetup

def start():
    auth.master_password_authentication()

def main():
    if not auth.master_password_authentication():
        return
    
    while True:
        print("\nPassword manager")
        print("1. Add a new password")
        print("2. View Saved Passwords")
        print("3. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            add_password()
        
        elif choice == '2':
            view_passwords()
            
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")
    
        
if __name__ == "__main__":
    main()