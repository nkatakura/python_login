#   FILENAME:   python_login.py
#   AUTHOR:     Naoki Katakura
#   DATE:       2021-09-22
#   DESCRIPTION:
#       Directions: "Create a login function that validates a users login and password.  You can start by hard coding the login and password in the code.
#       The next step would be to put the information in a file or database, and then to encrypt it using a python library."
#   
#       Login credentials are stored in local files named "usernames.txt" and "passwords.txt"
#       Credentials are checked by looping through each line of the file to find a match.
#       Passwords are saved by concatenating the username and password, then encrypting the combination, to tie usernames to passwords
#       The python library "cryptography" is used for encryption.

# TO DO:
#       Create a database to store login information
#           Currently login information is saved as a text file in the same directory.
#       Encrypt the database
#       Add something that can be done after logging in
#       Add error handling all around

import os
from cryptography.fernet import Fernet

# Encryption code:

def load_key():
    # This function loads a key that is stored on a local file.
    # This way encryption/decryption stays consistent

    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    # This function encrypts a message that is passed to it, and returns the encrypted message.
    # Note: the variable type that is returned is of Byte type, and is not a string

    key = load_key()
    encoded_message = message.encode()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(encoded_message)

    return encrypted_message

def decrypt_message(encrypted_message):
    #   This function decrypts a message that is passed to it.
    #   Note: a variable of type Byte must be passed or this will throw an error

    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)

    return decrypted_message

# File Handling code

def readFromFile(filename):
    #   Reads each line of a file and creates an array of those lines
    #   File can be chosen by passing the file name
    #   Returns the array of lines
    
    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    array = []

    f = open(filename, "r")
    for x in f:
        x = x.strip()
        array.append(x)

    f.close()

    return array

def writeToFile(filename, content):
    #   This function will write a line to a specified file
    #   File is specified by passing the file name
    #   What to write is passed after file name ("content" parameter)
    #   content is written to a line with a newline following it

    os.chdir(r"C:\Users\nkata\Documents\projects\python_login")
    f = open(filename, "a")
    f.write(str(content))
    f.write("\n")
    f.close()

def clearConsole():
    #   This function simply clears the console to make the menu more readable

    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_menu():
    #   This function prints the main menu, prompts the user for an option, then returns whatever option the user chose

    print("Select a menu option:")
    print("1. Create new login credentials")
    print("2. Login using existing credentials")
    print("3. Exit the application")
    userInput = input("Enter selection: ")
    return userInput

def checkUsernameExists(usernameToCheck):
    #   This function loops through each line in the "usernames.txt" file
    #   to check if the username passed to it exists in the file
    #   Returns the boolean value for if the username was found or not

    exists = False
    usernameArray = readFromFile("usernames.txt")
    for lineRead in usernameArray:
        lineRead = lineRead.strip()
        if lineRead == usernameToCheck:
            exists = True
    return exists

def checkPassword(passwordEntered):
    #   This function loops through each line in the "passwords.txt" file 
    #   to check if the password entered exists in the file
    #   Each line is read, decrypted, decoded (from bite to string) then compared to the argument

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
    #   This function prompts the user to enter the credentials they wish to have
    #   and enters the information into the appropriate files

    #   This function should actually be split up into two different ones
    #       One function to prompt and retrieve user input
    #       Another that prints the information into the files

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
    #   This function attempts to log the user in
    #   It will check the username and password they enter
    #   to see if it matches what is stored on the file

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