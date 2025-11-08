from cryptography.fernet import Fernet
from crypto import derive_key

def test_derive_key():
    password = "testpassword"
    salt = b"1234567890abcdef"
    fernet = derive_key(password, salt)
    assert isinstance(fernet, Fernet)