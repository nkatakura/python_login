#   FILENAME:   python_login.py
#   AUTHOR:     Naoki Katakura
#   DATE:       2021-09-22
#   DESCRIPTION:
#       Create a login function that validates a users login and password.  You can start by hard coding the login and password in the code.
#       The next step would be to put the information in a file or database, and then to encrypt it using a python library.

from cryptography.fernet import Fernet
import os

######################################################
password = "test"
key = Fernet.generate_key()
fernet = Fernet(key)
encodedPassword = fernet.encrypt(password.encode())


print("original string: ", password)
print("encrypted string: ", encodedPassword)
######################################################

# print menu

# Clears Console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_menu():
    clearConsole()
    print("Select a menu option:")
    print("1. Create new login credentials")
    print("2. Login using existing credentials")
    print("")


# create user

# login