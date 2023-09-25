"""
Team Members:
Adra Gonzalez
Savannah Ciak
Hannelore Sanokklis
Lily Pouliot
"""
import math

def start_conversion():
    print("You have the options to convert Binary to Hexadecimal (1), Binary to Base-10 (2), Hexadecimal to Base-10 (3), Hexadecimal to Binary (4), Base-10 to Binary (5), Base-10 to Hexadecimal (6)")
    conversion_type = int(input("What conversion do you want? Please enter an integer number between 1-6. Reference the options above."))

    if (conversion_type == 1):
        num = hex(int(input("What is the binary number?")))
        print(bin_to_hex(num))

    elif (conversion_type == 2):
        userinput = input("What is the binary number?")
        num = int(userinput, 2)
        print(bin_to_base10(num))

    elif (conversion_type == 5):
        num = int(input("What is the starting number?"))
        return (base10_to_bin(num))

    # num_type = input("Is this a Binary, Hexadecimal, or Base-10 number?")


def bin_to_hex(num):  # Option 1
    print(num)


def bin_to_base10(num):  # Option 2
    print(num)


def base10_to_bin(num):  # Option 5
    num5 = bin(num)
    print(num5)


start_conversion()
