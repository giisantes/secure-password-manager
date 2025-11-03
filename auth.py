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


    else: #logic for entering master password that has already been set
        input_password = input("Please enter your master password: ")
        stored_data = Path.read_text(masterpassfile).strip()
        