#Binary numbers in Python are always prepended with '0b'. 
#So instead of writing 101 you would write 0b101
#0b101 is equal to 5

print("The binary number 101 converts to:")
print(0b101)

#We can also add binary numbers
print("5 + 5 =")
print(0b101 + 0b101)

#or we can convert back and forth
numberOfDaysInWeek = 0b111
print("There are " + str(numberOfDaysInWeek) + " days in a week")
print("And 7 in binary is " + bin(7))

print(0b11111111)

print(0xff)

#Hexadecimal numbers in Python are always prepended with '0x'. 
#So instead of writing ff you would write 0xff
#0xff is equal to 255

print("The hexadecimal number ff converts to:")
print(0xff)

#We can also add binary numbers
print("11 + 13 =")
print(0xa + 0xc)

#or we can convert back and forth
numberOfDaysInYear = 0x16d
print("There are " + str(numberOfDaysInYear) + " days in a week")
print("And 365 in hex is " + hex(365))

#Convert 56 from decimal to hexadecimal
print(0b10010)
