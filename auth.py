__package__ = "auth"
import hashlib
import os
from pathlib import Path
import mastersetup

def hash_password(password: str, salt: bytes = None) -> tuple:

    if salt is None:
        # Generate a new random salt
        salt = os.urandom(16)

    # Hash the password with the salt using SHA-256
    password_hash = hashlib.sha256(salt + password.encode()).digest()
    #.encode converts the password string to bytes .digest() returns the binary hash value
    # returns the salt and the hashed password
    return salt.hex(), password_hash.hex()

def master_password_authentication():
    masterpassfile = Path(__file__).parent / "masterpass.hash"
    
    if not masterpassfile.exists(): # First time setup
        mastersetup.firsttimesetup()
        return master_password_authentication()


    else: #logic for entering master password that has already been set
        input_password = input("\nPlease enter your master password to login: ")
        stored_data = Path.read_text(masterpassfile).strip()
        stored_salt_hex, stored_password_hash_hex = stored_data.split(":")
        stored_salt = bytes.fromhex(stored_salt_hex)
        _, input_password_hash_hex = hash_password(input_password, stored_salt)
        if input_password_hash_hex == stored_password_hash_hex:
            print("Login successful.")
        else:
            print("Incorrect master password. Please try again.")
            return master_password_authentication()

