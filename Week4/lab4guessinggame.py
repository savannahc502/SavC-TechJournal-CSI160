"""This program picks a random number and has the user guess it.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 4 Lab: Guessing Game
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

from random import randint  # Imports the randint function to generate random numbers.
random_num = randint(0, 9)  # Generates a random number between 0-9

print("Welcome to Savannah's Number Guessing Game!")  # Intro message printed

guess = int(input("Guess an integer between 0 and 9: "))  # Asks for an integer input
# Assumption is that user inputs a valid integer value. Once we learn about data validation,
# we can better avoid traceback errors.

if guess == random_num:  # Checks to see if user input matches computer's random guess.
    print("You guessed correctly! The number was", random_num)
else:
    print("Sorry,", guess, "was the wrong number. It was:", random_num)
