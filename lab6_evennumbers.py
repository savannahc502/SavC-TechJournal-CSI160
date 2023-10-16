""" Prints the even numbers in a list, one per line

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

print("This is Code #2: ")


def print_even(numbers):
    """Prints the even numbers in a list, one per line

    :param numbers: (list) list of integers
    :return: None
    """
    print("These are the even numbers in the list, one per line: ")
    for i in numbers:  # for the parameter numbers, which is an integer list, each value is evaluated.
        if i % 2 == 0:  # If the value is even
            print(i)  # Prints the even number, one per line
        else:
            continue


numbers = [1, 2, 3, 4, 5, 6]  # Test code for the above function
# This code could be edited to take input from the user to build a list,
# but that was outside of the scope for this code.
even_numbers = print_even(numbers)
