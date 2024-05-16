"""This program converts a grade percentage into a letter grade.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 4 Lab: Grading Scale Conversion
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


def grade_conversion(grade_percent):
    """ This function converts a grade percentage to a letter grade.

            Arguments:
                grade_percent: the grade percentage the user would like
                to convert to a letter grade
            Returns:
                The letter grade string value of the grade percentage
            Assumptions:
                The user inputs a valid float grade value
     """
    if grade_percent >= 93:  # Begins an if statement chain that checks each possible letter grade
        letter_grade = "A"
    elif 90 <= grade_percent < 93:  # Using ranges to determine what letter grade the input is.
        letter_grade = "A-"
    elif 87 <= grade_percent < 90:
        letter_grade = "B+"
    elif 83 <= grade_percent < 87:
        letter_grade = "B"
    elif 80 <= grade_percent < 83:
        letter_grade = "B-"
    elif 77 <= grade_percent < 80:
        letter_grade = "C+"
    elif 73 <= grade_percent < 77:
        letter_grade = "C"
    elif 70 <= grade_percent < 73:
        letter_grade = "C-"
    elif 67 <= grade_percent < 70:
        letter_grade = "D+"
    elif 63 <= grade_percent < 67:
        letter_grade = "D"
    elif 60 <= grade_percent < 63:
        letter_grade = "D-"
    else:
        letter_grade = "F"  # Once all other possibilities have been checked, we can determine that the grade is an F.

    return letter_grade  # Returns the now converted value


grade_result = float(input("Please enter a grade percentage, as a float, between 0-100: "))  # Asking the user for input
result = grade_conversion(grade_result)  # Telling the interpreter to take the input from above,
# run it through the function, and assign the return value from the function to the variable x.
print("Your letter grade conversion is:", result)  # Prints the final result variable value.
