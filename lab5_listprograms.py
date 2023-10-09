"""Four function descriptions were given, and we had to code them so that they passed the testing scripts.

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 5 Lab Programming with Lists
Due Date: 10/6/23

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


def number_of_zeros(grades):
    """Given a list of grades, determines the number of grades that are 0%

    params:
    grades (list of floats) - The grades to search. Example [75, 82.5, 97, 0, 87.5]

    return (int) - the number of 0% grades
    """
    int = 0  # Setting the initial variable, as noted in the class conditionals_loops.py notes.
    for i in grades:  # Testing each index in grades
        if(i == 0):  # Testing each index in grades for equaling zero
            # Fixed from "grades == 0", which was turning up false.
            int = int + 1
        else:
            continue  # Required else statement, which continues the script.
    return int


def median(numbers):
    """Find the median of the given list of numbers.

    How to find the median:
    https://www.mathsisfun.com/median.html

    Note: Write your own implementation and do not use any libraries.  You will need to sort the list.

    params:
    numbers (list) A list containing either int or float elements

    return (numeric) The median value as either an int or float
    """
    numbers.sort()  # Need to sort the list before starting to find median. Sort function from lists.py class notes

    # The provided website states that finding the median requires knowing if the amount of numbers is odd or even.
    # If odd, the middle number is median. If even, the average of the two middle is the median.

    length = len(numbers)
    if (length % 2 == 1):  # % Modulus, gives the remainder. By dividing by two as a modulus, the remainder
        # is 1 if the length of the list is odd and 0 if the list is even.
        # Used the link below to find how to determine odd from even length.
        # https://www.codingninjas.com/studio/library/check-whether-the-length-of-given-linked-list-is-even-or-odd
        numeric = numbers[length // 2]
        # When the length is odd, we need the middle index.
        # // is a floored quotient, which will yield the result rounded down.
        # This rounded down result will be the middle index (since the indexing starts at 0 in a list).
    else:
        even_num1 = numbers[(length // 2)-1]  # Takes the index before the middle (since there is no "middle number").
        even_num2 = numbers[length // 2]  # Takes the index after the middle.
        numeric = (even_num1 + even_num2) / 2  # Taking the two middle index values and calculates the average.
    # Advice for the else statement given by student Sierra Blume on 10/8/23

    return numeric


def top_quartile(grades):
    """Return the top 25% of the grades in the supplied list of grades.
    Round up when determining how many grades to include in the top 25%.

    Hint: You will need to sort the list of grades

    params:
    grades (list of floats) Example [75, 82.5, 97, 0, 87.5]

    return (list of floats) - The top 25%
    """
    grades.sort()  # Sorts the grades from least to greatest. Need the top 25% from the right.
    length = len(grades)  # Determines the length of the grades list.

    if (length % 4 == 0):
        quart = length // 4
    elif (length % 4 != 0):
        quart = (length // 4) + 1
    else:
        pass

    top_25 = grades[-quart:]
    # Negative indexes pull from the ending of the list. So, the -quart is pulling the last fourth.
    # Personal Notes: https://github.com/savannahc502/SavC-TechJournal-CSI160/wiki/Week-5%3A-Lists#negative-indexes
    # The colon indicates I want to get a slice of a list.
    # https://www.techwithtim.net/tutorials/python-programming/beginner-python-tutorials/slice-operator

    return top_25

def domain_name_extractor(url):
    """Given an url, return the domain name

    You will need to utilize the .find method to complete this https://docs.python.org/3/library/stdtypes.html#str.find

    Hint: Find the starting point of the domain name, then find the end point.
    params:
    url (string) the url to search. Example: https://docs.python.org/3/library

    return (string) The domain name or IP address. Example: docs.python.org
    """
     y = url.find('c')
    domain1 = url[y:]

    z = domain1.find('/')

    string = domain1[0:z]
    return string

def test_number_of_zeros():
    print('Running number_of_zeros tests:')
    print('Test 1 passed -', number_of_zeros([75.0, 0.0, 97.0, 0.0, 87.5]) == 2)
    print('Test 2 passed -', number_of_zeros([]) == 0)


def test_median():
    print('Running median tests:')
    print('Test 1 passed -', median([10, 5, 8, 4, -1]) == 5)
    print('Test 2 passed -', median([10, 8, 4, -1]) == 6)


def test_top_quartile():
    print('Running top_quartile tests:')
    print('Test 1 passed -', top_quartile([97, 92.5, 84, 79, 67]) == [92.5, 97])
    print('Test 2 passed -', top_quartile([92.5, 86, 89, 75]) == [92.5])


def test_domain_name_extractor():
    print('Running domain_name_extractor tests:')
    print('Test 1 passed -',
          domain_name_extractor('https://champlain.instructure.com/courses/8933') == 'champlain.instructure.com')
    print('Test 2 passed -', domain_name_extractor('ftp://champlain.edu/myfile.pdf') == 'champlain.edu')


print('Running Unit Tests\n')
test_number_of_zeros()
print()
test_median()
print()
test_top_quartile()
print()
test_domain_name_extractor()
