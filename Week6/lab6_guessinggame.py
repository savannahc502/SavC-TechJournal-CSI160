""" Five prompts were given, and we were tasked with completing the code to get the
desired results.

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

print("This is Code #3: ")

from random import randint  # Imports the randint function to generate random numbers.
randomNum = randint(0, 100)  # Generates a random number between 0-100

print("Welcome to Savannah's Number Guessing Game!")  # Intro message printed

# Asks for an integer input
# Assumption is that user inputs a valid integer value. Once we learn about data validation,
# we can better avoid traceback errors.

x = True  # Helps set up the while loop
while x == True:  # Sets the while loop in motion
    guess = input("Guess an integer between 0 and 100: ")
    if guess.isdigit():  # Checks that the input number is a digit.
        guess = int(guess)  # Converts input into an integer (not sure if this is needed?)
        if guess == randomNum:
            print("You were correct! The random number was", randomNum)
            x = False  # Closes the while loop: the guessing will keep
            # continuing until the guess matches the random number.
        if guess > randomNum:  # Tells the user that the guess was higher
            print("Your number,", guess, "is higher than the random number. Try again!")
        if guess < randomNum:  # Tells the user that the guess was lower
            print("Your number,", guess, "is lower than the random number. Try again!")
    else:   # Data validation: if the guess is not a digit, the else statement will print
        # and loop back to asking for input.
        print("Try again!")
        continue
