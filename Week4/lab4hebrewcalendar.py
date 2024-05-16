"""Computes if a given year is a leap year in the Hebrew Calendar

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 4 Lab: Hebrew Calendar
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


def is_hebrew_leap_year(year):
    """ This function converts a grade percentage to a letter grade.
        Arguments:
            year: integer input of the user
        Returns:
            True: the year is a leap year
            False: the year is not a leap year
        Assumptions:
            User inputs a valid integer value
        """
    if year % 19 == 0 or 3 or 6 or 8 or 11 or 14 or 17:
        return True
    else:
        return False


print("Welcome! Here, you can check if a given year is/will be a leap year in the Hebrew Calendar.")
year_input = int(input("Please type in the year as an integer:"))
print("The outcome is:", is_hebrew_leap_year(year_input))
