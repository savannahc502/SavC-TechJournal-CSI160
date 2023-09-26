"""This file can convert binary, hexadecimal, and base-10 integer inputs into each other.

Authors: Adra Gonzalez, Savannah Ciak, Hannelore Sanokklis, Lily Pouliot
Class: CSI-160-01
Assignment: Class Exercise 1
Due Date: 21 September 2023

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


def start_conversion():
    print('''You have the options to convert:
    Binary to Hexadecimal (1)
    Binary to Base-10 (2) 
    Hexadecimal to Base-10 (3)
    Hexadecimal to Binary (4)
    Base-10 to Binary (5)
    Base-10 to Hexadecimal (6)''')  # A comment block was used to improve formatting

    conversion_type = int(input("What conversion do you want? Please enter an integer number between 1-6. Reference the options above."))

    if conversion_type == 1:
        num = int(input("What is the binary number?"), 2)  # In int(x, 2) the 2 is used to show
        # that the input is a base 2 (binary) number
        print("The hexadecimal number is:", bin_to_hex(num))

    elif conversion_type == 2:
        num2 = int(input("What is the binary number?"), 2)
        print("The base-10 number is:", bin_to_base10(num2))

    elif conversion_type == 3:
        num3 = int(input("What is the Hexadecimal number?"), 16)
        print("The base-10 number is:", hex_to_base10(num3))

    elif conversion_type == 4:
        num4 = int(input("What is the hexadecimal number?"), 16)
        print("The binary number is:", hex_to_bin(num4))

    elif conversion_type == 5:
        num5 = int(input("What is the base-10 number?"))
        print("The binary number is:", base10_to_bin(num5))

    elif conversion_type == 6:
        num6 = int(input("What is the base-10 number?"))
        print("The hexadecimal number is:", base10_10_hex(num6))


def bin_to_hex(num):  # Option 1
    num = hex(num)
    return num


def bin_to_base10(num2):  # Option 2
    num2 = int(num2)
    return num2


def hex_to_base10(num3):  # Option 3
    num3 = int(num3)
    return num3


def hex_to_bin(num4):  # Option 4
    num4 = bin(num4)
    return num4


def base10_to_bin(num5):  # Option 5
    num5 = bin(num5)
    return num5


def base10_10_hex(num6):  # Option 6
    num6 = hex(num6)
    return num6


start_conversion()
