""" Password manager that does simple "encryption"

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 10/11: Password Manager
Due Date: 11/10/23

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


# Encrypting the Password for add_entry()
# https://github.com/savannahc502/SavC-TechJournal-CSI160/wiki/Week-10%3A-Dictionaries%2C-ASCII%2C-Caesar-Cipher#the-chr-and-ord-functions-can-convert-between-characters-and-ordinals
# https://www.geeksforgeeks.org/program-to-find-the-xor-of-ascii-values-of-characters-in-a-string/
# Was given advice for the password encryption and decryption by student Jess Hansard of UVM
def encrypt_password(password, key):
    encrypted_password = ''.join(chr(ord(char) ^ ord(key)) for char in password)
    return encrypted_password
# Iterates through each character in the password string and applies an XOR operation between
# the ASCII value and the corresponding character (kind of like ceaser cypher but with the ASCII alphabet).


# Decrypting the password for lookup_entry()
def decrypt_password(encrypted_password, key):
    decrypted_password = ''.join(chr(ord(char) ^ ord(key)) for char in encrypted_password)
    return decrypted_password


# Function to add a new entry to the password manager (choice 1 of main() function)
def add_entry(passwords, key):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Checks to make sure all three variables above have input
    if website == "" or username == "" or password == "":
        print("Please enter something. Restarting the program now.")
        return
    # Checks if the password is complex by calling the is_password_complex() function
    elif not is_password_complex(password):
        print("Password does not meet complexity requirements.")
        return  # If the password is not complex, the main() while loop continues
    else:
        # Encrypts the complex password by calling on the encrypt_password() function
        encrypted_password = encrypt_password(password, key)

        # Add entry to the previously empty passwords dictionary in the main() function
        passwords[website] = {'username': username, 'password': encrypted_password}
        # https://www.geeksforgeeks.org/python-key-index-in-dictionary/
        print("Entry added successfully.")


# Function to look up and print information about an entry in the passwords dictionary (choice 2 of main() function)
def lookup_entry(passwords, key):
    website = input("Enter website to lookup: ")  # Asks for the website to lookup
    try:
        entry = passwords[website]  # Looks for that website index in the passwords dictionary
        decrypted_password = decrypt_password(entry['password'], key)  # Decrypts password by calling the
        # decrypt_password() function and using the entry variable
        print(f"Website: {website}\nUsername: {entry['username']}\nPassword: {decrypted_password}")
        # F-String Formatting:
        # https://github.com/savannahc502/SavC-TechJournal-CSI160/wiki/Week-8-9%3A-Midterm-and-Two-Dimensional-Lists#formatting-strings
    except KeyError:  # KeyError is when you call something in a dictionary that does not exist.
        print(f"No entry found for {website}.")  # Says the website entry does not exist, while loop continued in main()


# Function to delete an entry (choice 3 of main() function)
def delete_entry(passwords):
    website = input("Enter website to delete: ")  # Asks user for entry to delete

    try:
        del passwords[website]  # Deletes that index.
        print(f"Entry for {website} deleted successfully.")
    except KeyError:  # KeyError is when you call something in a dictionary that does not exist.
        print(f"No entry found for {website}.")  # Says the website entry does not exist, while loop continued in main()


# Function to check password complexity (used for add_entry() function)
def is_password_complex(password):
    if len(password) < 8 or not any(char.isupper() for char in password) or not any(
            char in "!@#$%^&*()_-+=<>,.?/:;{}[]|\\~" for char in password):
        # https://www.geeksforgeeks.org/python-any-function/
        # https://github.com/savannahc502/SavC-TechJournal-CSI160/blob/main/data_validation.py
        # Was given advice to use the "char" ability by Jess Hansard, student at UVM
        # If the length of the password is less than 8, no characters are uppercase, and no special characters as
        # specified above, the password is not complex enough.
        print("Password complexity requirements not met:")
        print(" - Minimum length: 8 characters")
        print(" - At least one uppercase letter")
        print(" - At least one special character")
        return False  # False if not complex
    return True  # True if complex


# Start of Code: Main function and User Input Dashboard
def main():
    passwords = {}  # Creates the empty dictionary 'passwords'

    key = input("Enter an encryption key between 1 and 9: ")  # Asks for user input of ceaser cypher "encryption"
    try:
        if 1 <= int(key) <= 9:  # Confirms user input 1-9
            pass
        else:
            print("That is not a valid input. Enter a integer 1-9. Please run the code again.")
            return  # Stops Code if user input is an integer, but is not 1-9.
    except ValueError:
        print("That is not a valid input. Please run the code again.")
        return  # Stops Code is user input is not an integer

    while True:  # Prints menu for user
        print("\nPassword Manager Menu:")  # \n for formatting - creates a blank line.
        print("1. Add Entry")
        print("2. Lookup Entry")
        print("3. Delete Entry")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")  # Choose an option above and assigns it the variable "choice"

        if choice == "1":
            add_entry(passwords, key)  # Calls add_entry function (see above)
        elif choice == "2":
            lookup_entry(passwords, key)  # Calls lookup_entry function (see above)
        elif choice == "3":
            delete_entry(passwords)  # Calls delete_entry function (see above)
        elif choice == "4":
            print("Quitting.")  # Uses break to stop the while loop, which will end the code.
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")  # If choice is not 1-4, prints this and
            # while loop continues.


main()  # Start of the code, calls the main() function.
