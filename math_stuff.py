# Working with the math module, binary, and hex values.
# 9/14/23

import math  # Only becomes active once a command calls it.
x = 2**3  # Two asterisks will make an exponent
# print(x)

my_pi = 22/7  # Close to Pi
real_pi = math.pi  # Pulls the actual value of Pi

# print(my_pi)
print("The real value of pi is", real_pi)

exp = math.pow(1.5, 2)  # The first value is the number, the second value is the exponent.
# print(exp)

# Take the square root of 49 and 50
y1 = math.sqrt(49)
y2 = math.sqrt(50)
# print(y1, y2)

bin_num1 = 0b111  # Prefix binary values with 0b
bin_num2 = 0b111011
result = bin_num1 + bin_num2  # Binary values added and then converted into a base-10 value.
result = bin(result)  # The bin() converts a base-10 value into a binary value.
# print(result)

hex1 = 0xfff  # Prefix hexadecimal values with 0x
# print(hex1)
base10 = 365015
hex2 = hex(base10)  # Converts the base 10 value into hex value
# print("The hex value of", base10, "equals", hex2)

binvalue = bin(base10)
# print("The binary value of", base10, "equals", binvalue)

# Controlling decimal output
real_pi = format(math.pi, ".2g")  # give 2 significant digits
print(real_pi)
real_pi = format(math.pi, ".4f")  # rounds to 4 decimal places
print(real_pi)
