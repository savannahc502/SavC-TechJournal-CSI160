# 9/4/23, 9/7/23 Savannah Ciak
# This is a comment, the interpreter will not process it as code
# To create a block comment, use quote marks as seen below

"""
Here is a block comment
It takes up two lines.
"""

'''
Here is another block comment
Using a series of three single quotes
'''

"""
Four Basic Data Types: 
String --> "Hello World", "5"
Integer --> 5
Float --> 5.12
Boolean --> True False, 1 and 0

Variable Names Rules: 
No Spaces
Never start with a number
Do not use special characters

PEP8 Standard!
"""

"""
Basic Functions: 
print()
str() --> converts an integer data type to string
int() --> converts a string data type to an integer
len() --> return the total number of character in a variable
float() --> converts integer/strings into a float
input() --> allows for user input
"""

# A Variable
num1 = 2
num2 = 8  # If this was "8", it would not work because that would be a string, not an integer.

result1 = num1 * num2
result1 = num2 / num1  # Variable Reassignment
result2 = num1 / num2
# print(result) Creates a Traceback error because the variable does not exist
# print(result2)

name = "John Doe"
address = '1 Main Street'
title = "Book = 'Python Programming'"  # Nesting Quote Marks
age = 22  # Integer data type - you cannot add string with an integer, must use a conversion function.
experience = "22"

# print(name + "is" + str(age) + "years old")  # Mixing string with variable output - concatenates
# print(name, "is", age, "years old.")  # str() conversion not needed bc not using a mathematical operation

# first_name = input("Enter your name:")
# n1 = int(input("Enter your first number:"))  # The integer function will translate the input from string to an integer
# n2 = input("Enter your second number:")
# n2 = int(n2)  # The integer function will translate the input from string to an integer
# n3 = n1 + n2
# print("Hi,", first_name + ".", "The addition of these numbers equals", n3)

# length = len(title)  # Counts the single quotes above in the variable title because it's not acting as a function.
# print("The number of characters in the variable 'title' equals:", length)

grade1 = 3.75
grade2 = 3.25
grade3 = 3.01
grade4 = 3.00
grade5 = 0
courses = 5
statement = "The average GPA equals:"

"""
My code attempt at making the program calculate gpa:

first_name = input("Enter your name:")
print("Hi,", first_name + ".")
grade5 = float(input("I know your first four classes' gpas. What is your fifth class's gpa?:"))

avg = (grade1+grade2+grade3+grade4+grade5)/courses
print("Thank you!", statement, avg)

This works! Below is the class: 
"""

avg = ""
grade5 = float(input("Please enter the fifth class GPA:"))
sum = grade1 + grade2 + grade3 + grade4 + grade5
avg = sum/courses
print(statement, avg)
