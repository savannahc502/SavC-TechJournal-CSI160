"""This python file holds some basic functions that do very basic mathematical functions.
The purpose of this code is to practice with how functions take input and give output.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 3: Lab - Functions
Due Date: 22 September 2023

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
import math
# Sierra Blume, a student here at Champlain College, helped me in understanding the concept of parameters in a
# function. I did create the functions on my own, however she helped guide me through the first function
# call for interest_rate so that I could understand the concept better.


def interest_rate(loan):
    """This function calculates a 5.5% interest rate on a given number

    Arguments:
        loan (float): the dollar amount of loans the user will take out for school

    Returns:
        The total loan amount after one year at a 5.5% interest rate

    Assumptions:
        Assumes loan is a float
        Assumes the user omits the $ sign
    """
    return loan * 1.055


def can_usa_conversion(money):
    """This function converts U.S. currency to Canadian Currency

    Arguments:
        money (float): the total amount of money the user has in U.S. currency

    Returns:
        The total amount of money the user has in Canadian currency

    Assumptions:
        Assumes money is a float
        Assumes money is in U.S. currency
        Assumes the user omits the $ sign
    """
    return money * 1.26  # Conversion rate found at https://www.cuemath.com/calculators/usd-to-cad-calculator/.


def py_theo(num1, num2):
    """This function calculates a hypotenuse of a triangle given to sides.

       Arguments:
           num1 (float): the first side of the triangle
           num2 (float): the second side of the triangle

       Returns:
           The hypotenuse of the triangle

       Assumptions:
           Assumes num1 is a float
           Assumes num2 is a float
           Assumes the user can pick random numbers
       """
    return math.sqrt(math.pow(num1, 2) + math.pow(num2, 2))


# Usage 1:
print("Welcome to the Bank Of Savannah! We're so glad to take your money!")
loanAmount = float(input("How much money will you be taking out for school in loans (omit the $ sign): "))
print("\nThe total amount you will owe after the first year of interest will be:", "$", interest_rate(loanAmount))
print("Phew! 5.5% adds up real quick! Glad I'm not a student.")

# Usage 2:
canadianAmount = float(input("\nHow much money do you have right now in U.S. currency (omit the $ sign): "))
print("The total amount you have in Canadian currency is", "$", can_usa_conversion(canadianAmount))

# Usage 3:
print("\nBanks do math, right? What's better than Pythagorean's Theorem!")
aSquared = float(input("Pick a number:"))
bSquared = float(input("Pick a second number:"))
print("If those two numbers were the sides of a triangle, the hypotenuse length would be", py_theo(aSquared, bSquared))

print("\nThanks for your data! We're going to go sell your credit info now :)")
