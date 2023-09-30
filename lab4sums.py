"""This program asks for two numbers and determines if the sum
is less than or greater than 100.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 4 Lab: Sums and 100
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


def sums(num1, num2):
    """ This function converts a grade percentage to a letter grade.
    Arguments:
        num 1: The first float input from the user.
        num 2: The second float input from the user
    Returns:
        outcome: The sums of the two numbers if less than 100. If more than 100, returns string.
    Assumptions:
        User inputs valid float inputs
    """
    if num1 + num2 > 100:
        outcome = "They add up to a big number!"
    else:
        outcome = "They add up to: " + str(num1 + num2)
    return outcome


input1 = float(input("Please enter your first number: "))
input2 = float(input("Please enter your second number: "))
result = sums(input1, input2)
print(result)
