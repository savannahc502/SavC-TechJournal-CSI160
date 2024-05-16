""" Returns a list of phone numbers with the area code added.

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

print("This is Code #1: ")


def add_area_code(phone_numbers, area_code):
    """Returns a list of phone numbers with the area code added.
    Given a list of phone numbers that are missing the area code,
    append the area code to the phone numbers in the list and return the result list.

    :param phone_numbers: (list) A list of phone numbers (strings) that do not have the area code
                                Example: ['555-1212']
    :param area_code: (str) The area code to add Example: '802'
    :return: (list) A list of phone numbers with the area code Example: ['802-555-1212']
    """
    area_code_phone_numbers = []  # Creates a new empty list

    for i in phone_numbers:  # For loop that examines all index values in the phone_numbers list
        area_code_phone_numbers.append(area_code + i)
        # Calls on the new list to be appended with the values of area_code ("802-") followed by
        # an index value. Since this is in a for loop, this will be done to each index.

    return area_code_phone_numbers  # Returns the new list


# Best Practice Tip: Making a copy of the original list will allow you to return a list with area codes
# without modifying the original list.
# example usage
phone_numbers = ['555-1212', '999-0738']
with_area_code = add_area_code(phone_numbers, '802-')
print(with_area_code)
