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
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    usernameFile = open("usernames.txt", "r")
    exists = False
    for fileLine in usernameFile:
        fileLine = fileLine.strip()
        if usernameToCheck == fileLine:
            exists = True
    return exists

def checkPassword(passwordEntered):
    valid = False
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    passwordFile = open("passwords.txt", "r")
    for fileLine in passwordFile:
        fileLine = fileLine.strip()
        if fileLine == passwordEntered:
            valid = True
    passwordFile.close()
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
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    usernameFile = open("usernames.txt", "a")
    usernameFile.write(usernameEntered + "\n")
    usernameFile.close
    usernameAndPassword = usernameEntered + passwordEntered
    passwordFile = open("passwords.txt", "a")
    passwordFile.write(usernameAndPassword + "\n")
    passwordFile.close

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