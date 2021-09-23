#   FILENAME:   python_login.py
#   AUTHOR:     Naoki Katakura
#   DATE:       2021-09-22
#   DESCRIPTION:
#       Create a login function that validates a users login and password.  You can start by hard coding the login and password in the code.
#       The next step would be to put the information in a file or database, and then to encrypt it using a python library.

# TO DO:
#       Create a database to store login information
#           Currently login information is saved in plain text as a text file in the same directory.  This is terrible for security
#       Encrypt the database
#       Add something that can be done after logging in

import os
from cryptography.fernet import Fernet

# Encryption code:

def load_key():
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):

    key = load_key()
    encoded_message = message.encode()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(encoded_message)

    return encrypted_message

def decrypt_message(encrypted_message):

    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)

    return decrypted_message

# File Handling code

def readFromFile(filename):
    # returns an array of lines from the code
    
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    array = []

    f = open(filename, "r")
    for x in f:
        x = x.strip()
        array.append(x)

    f.close()

    return array

def writeToFile(filename, content):
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    f = open(filename, "a")
    f.write(str(content))
    f.write("\n")
    f.close()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_menu():
    print("Select a menu option:")
    print("1. Create new login credentials")
    print("2. Login using existing credentials")
    print("3. Exit the application")
    userInput = input("Enter selection: ")
    return userInput

def checkUsernameExists(usernameToCheck):
    exists = False
    usernameArray = readFromFile("usernames.txt")
    for lineRead in usernameArray:
        lineRead = lineRead.strip()
        if lineRead == usernameToCheck:
            exists = True
    return exists

def checkPassword(passwordEntered):
    valid = False
    passwordArray = readFromFile("passwords.txt")
    for lineRead in passwordArray:
        lineRead = lineRead.strip()
        lineRead = decrypt_message(eval(lineRead))
        lineRead = lineRead.decode()
        if lineRead == passwordEntered:
            valid = True

    return valid

def createLogin():
    usernameValid = False
    while usernameValid == False:
        clearConsole()
        usernameEntered = input("Enter desired username: ")
        if checkUsernameExists(usernameEntered):
            print("ERROR! That username has already been taken, please choose a new one.")
        else:
            usernameValid = True
    clearConsole()
    print("Username chosen: ", usernameEntered)
    passwordValid = False
    while passwordValid == False:
        passwordEntered = input("Enter desired password: ")
        passwordValidation = input("Enter desired password again: ")
        if passwordEntered == passwordValidation:
            passwordValid = True
        else:
            print("ERROR! Passwords did not match, please re-enter.")
    writeToFile("usernames.txt", usernameEntered)
    usernameAndPassword = usernameEntered + passwordEntered
    usernameAndPassword = encrypt_message(usernameAndPassword)
    writeToFile("passwords.txt", usernameAndPassword)

def login():
    usernameValid = False
    while usernameValid == False:
        usernameEntered = input("Enter username: ")
        if checkUsernameExists(usernameEntered) == False:
            print("ERROR! Username not found in records.  Please try again")
        else:
            usernameValid = True
    passwordValid = False
    while passwordValid == False:
        passwordEntered = input("Please enter your password: ")
        if checkPassword(usernameEntered + passwordEntered) == False:
            print("ERROR! Incorrect password, please try again: ")
        else:
            passwordValid = True
    return usernameEntered

def main():
    keepGoing = True
    while keepGoing:
        clearConsole()
        choice = print_menu()
        if choice == "1":
            createLogin()
        elif choice == "2":
            username = login()
            print("You are now logged in as: ", username)
            input("Press enter to continue...")
        else:
            keepGoing = False

main()