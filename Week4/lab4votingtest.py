"""This program runs a simple if/then statement that determines if the user
is of the legal voting age of 18+.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 4 Lab: Voting Age
Due Date: 9/29/23

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


def voting_age():  # No arguments, but if statements make more sense to me in a function format
    """ Tells the user if they are of voting age or not.

         Assumptions:
            User inputs a valid integer value
            User knows their age
    """
    x = input("Enter your age as an integer number:")
    # ^ Asks for an input and assigns it to the variable x
    if x == "":  # Checks if the user entered nothing
        print("You did not enter anything. Please restart.")
    # Begins an if statement chain that goes through age ranges.
    else:
        x = float(x)  # Converts the x variable string input to a float.
        if x <= 0:
            print("Your age is", x, "-- do you even exist?")  # Questions the user if they entered a grade less than 0.
        elif x < 18:
            print("Your age is", x, " -- You must be 18 to vote.")  # Tells the user that they cannot vote under 18.
        elif x > 110:
            print("Your age is", x, "-- are you a vampire?")  # Questions the user if they put a large number for age.
        elif x >= 18:
            print("Your age is", x, "-- You are of voting age.")  # Tells the user that they can vote.


voting_age()
