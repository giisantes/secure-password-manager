__package__ = "mastersetup"
import auth
from pathlib import Path

def set_master_password():
    
    master_password = input("\nPlease set your master password: ")

    if len(master_password) < 8: 
        print("Password must be at least 8 characters long. Please try again.")
        return set_master_password()
    
    elif len(master_password) > 64:
        print("Password must be less than 64 characters long. Please try again.")
        return set_master_password()

    elif not any(char.isdigit() for char in master_password):
        print("Password must contain at least one number. Please try again.")
        return set_master_password()
    
    elif not any(char.isupper() for char in master_password):
        print("Password must contain at least one uppercase letter. Please try again.")
        return set_master_password()
    
    elif not any(char.islower() for char in master_password):
        print("Password must contain at least one lowercase letter. Please try again.")
        return set_master_password()
    
    else: 
        confirm_password = input("Please confirm your master password: ")
        if master_password != confirm_password:
            print("Passwords do not match. Please try again.")
            return set_master_password()
        elif master_password == confirm_password:
            masterpassfile = Path(__file__).parent / "masterpass.hash"
            hashed_salt, hashed_password = auth.hash_password(master_password)
            Path.write_text(masterpassfile, f"{hashed_salt}:{hashed_password}")
            print("Master password set successfully.")
            
def firsttimesetup():
    print("\nAs this is your first time running the application you will need to set a master password. \nThis will be needed to access your stored passwords in the future.")
    set_master_password()

