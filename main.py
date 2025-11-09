import auth
import mastersetup
import menuoptions
from menuoptions import add_password, view_passwords

def start():
    auth.master_password_authentication()

def mainn():
    
    cipher = auth.master_password_authentication()

    if not cipher:
        return
    
    while True:
        print("\nPassword manager")
        print("1. Add A New Password")
        print("2. View Saved Passwords")
        print("3. Clear All Saved Passwords")
        print("4. View All Saved Passwords")       
        print("5. Exit")
        
        choice = input("\nPlease select an option: ")
        
        if choice == '1': 
            add_password(cipher)
        
        elif choice == '2':
            view_passwords(cipher)

        elif choice == '3':
            confirm = input("\nAre you sure you want to clear all saved passwords? This action cannot be undone. (yes/no): \n").strip().lower()
            
            if confirm == 'yes':
    
                confirmPassword = input("Please enter your master password to confirm: \n").strip()
                
                if auth.verify_master_password(confirmPassword):
                    menuoptions.clear_passwords()
                    print("All saved passwords have been cleared.")
                
                elif not auth.verify_master_password(confirmPassword):
                    print("Master password is incorrect.")
                    print("Clear passwords operation cancelled.")
                    continue

            else:
                print("Clear passwords operation cancelled.")
                continue
            
        elif choice == '4':
            menuoptions.view_all_passwords(cipher)

        elif choice == '5':
            print("\nExiting the application. Goodbye!\n")
            break
            
        else:
            print("Invalid choice. Please try again.")
    
        
if __name__ == "__main__":
    mainn()