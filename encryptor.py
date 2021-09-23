# Test code for figuring out encrypting decrypting

from cryptography.fernet import Fernet
import os

def generate_key():
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()