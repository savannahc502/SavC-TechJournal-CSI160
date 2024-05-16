# Working with loops

mixedList = ["john", "sally", "sam", "Larry", "Mary", 1, 2, 6, 7, 9, 0, 2, 4, 5]
title = "Python Programming"

''''
for i in mixedList:
    print("The item in this list is:", i)  # Prints a single line for each list item
'''

'''
spam = 0
if (spam < 5):
    print('Hello, world.')
    spam = spam + 1
else:
    print("You fail if you forget the 'else' statement!")
'''

'''
# The 'while' loop
x = 0
while x < 5:
    print(x)
    x = x + 1
'''

'''
for j in range(5):  # The 5 indicates to loop from zero up to but not include the value in the function. 
    # Same rule for negatives - will assume a start at zero. 
    print(j)
'''

'''
for k in range(-5, 5):  # The loop starts at -5 and goes up to but does not include 5
    # Cannot get it to go in a negative direction > (5, -5) would print nothing
    print(k)
'''

for l in range(10, -20, -2):  # The first value is the starting point, the second value is the "up to but not include"
    # value, and the third is an incrementor. This is the exception for counting in negatives -- it can now tell
    # that you are counting in negatives and does not need to assume positive counting by one.
    print(l)
