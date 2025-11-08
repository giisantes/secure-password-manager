__package__ = "auth"
import hashlib
import os
from pathlib import Path
import mastersetup
from crypto import derive_key
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def hash_password(password: str, salt: bytes = None) -> tuple:

    if salt is None:
        # Generate a new random salt
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )

    password_hash = kdf.derive(password.encode())
    return salt.hex(), password_hash.hex()

def master_password_authentication():
    masterpassfile = Path(__file__).parent / "masterpass.hash"
    
    if not masterpassfile.exists(): # First time setup
        mastersetup.firsttimesetup()
        return master_password_authentication()

    input_password = input("\nPlease enter your master password: ")
    stored_data = Path.read_text(masterpassfile).strip()
    stored_salt_hex, stored_password_hash_hex = stored_data.split(":")
    stored_salt = bytes.fromhex(stored_salt_hex)
    _, input_password_hash_hex = hash_password(input_password, stored_salt)
   
    if input_password_hash_hex == stored_password_hash_hex:
        print("Login successful.")
        cipher = derive_key(input_password, bytes.fromhex(stored_salt_hex))
        return cipher
    else:
        print("Incorrect master password. Please try again.")
        return master_password_authentication()

