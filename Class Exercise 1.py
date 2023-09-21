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
    conversion_type = input("What converstion do you want? Please enter an integer number between 1-6. Reference the options above.")
    if(conversion_type == 1):
        num = bin(int(input("What is the starting number?")))
        return (Bin_to_Hex(num))

    elif(conversion_type == 5):
        num = int(input("What is the starting number?"))
        return (base10_bin(num))

    """elif(conversion_type == 2):
    elif(conversion_type == 3):
    elif(conversion_type == 4):
    
    elif(conversion_type == 6):"""
    num = input("What is the starting number?")
    #num_type = input("Is this a Binary, Hexadecimal, or Base-10 number?")

def Bin_to_Hex(num):
    print(num)

def base10_bin(num):
    num5 = bin(num)
    print(num5)
    
print(start_conversion())