# Understanding variable scope
import my_modules


y = 0  # Global variable, available to all functions. Problems are encountered when
# the global variable is used in a function and its value is changed


def my_function():
    global y
    y = y + 2  # Not allowed due to the fact that code is changing the value of a global variable
    x1 = 1  # Local Variable, only accessible to this function


# An example of encapsulating scope
def outside_function():
    x2 = 2
    print("This is the value as defined in the outside_function():", x2)

    def inner_function():
        x2 = 10  # Not great practice but this will work
        print("This is the value of x2 from the inner_function():", x2)

    inner_function()

# outside_function()


# Cannot create a function that is the name of a built-in -- can't my def math
def my_math():
    r = int(input('Radius:'))
    area = r**2*my_modules.p  # The variable 'p' sits in the my_modules file.
    # Prefix the calling of this variable by its module location.
    print('The area of a square equals:', area)


my_math()

for i in my_modules.x:
    print(i)