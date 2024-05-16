""" Asks the user for input to compile a list.
Then, prints the list with all the items separated
by a comma and a space, with and inserted before the last item.

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

listToPrint = []  # Creates a new list
while True:  # While loop was given by instructions
    newWord = input("Enter a word to add to the list (press return to stop adding words): ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

if len(listToPrint) == 1:  # If there's only one item in the list, a simple print is needed.
    print("The list is:", listToPrint[0])
else:  # If the list is longer than one item
    item_in_list = ""  # Creates an open variable
    for index, i in enumerate(listToPrint):  # Enumerate function to check index and value at same time.
        if i == listToPrint[-1]:  # Checks for the last list index using negative indexing!
            item_in_list = item_in_list + "and " + i
            # For the last item in the list, and is concatenated to it
            # https://www.geeksforgeeks.org/python-program-to-concatenate-all-elements-of-a-list-into-a-string/
        else:
            item_in_list = item_in_list + i + ", "
            # For all other items in the list, a comma is concatenated to it
    print(item_in_list)
