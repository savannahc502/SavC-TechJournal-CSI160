""" There is a list that the program acts like is a backpack. User can check if there is
an item in the backpack, or add an item to the backpack list.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 6 Lab: Loops
Due Date: 10/12/23

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

import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()  # Asks for user input of choice and assigns it to the variable userChoice

    if (userChoice == "1"):
        print("What item do you want to add to the backpack?")
        itemToAdd = input()  # Assigns the input to a variable
        itemsInBackpack.append(itemToAdd)  # Adds the input to the backpack list
        print("The backpack now contains: ", itemsInBackpack)  # Prints the new list contents

    if (userChoice == "2"):
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()  # Assigns the input to a variable
        if itemToCheck in itemsInBackpack:  # Checks if the input is in the list
            # https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
            print(itemToCheck, "is in the backpack.")
        elif itemToCheck not in itemsInBackpack:  # Checks if the input is not in the list
            print(itemToCheck, "is not in the backpack.")

    if (userChoice == "3"):
        sys.exit()

    else:
        continue
