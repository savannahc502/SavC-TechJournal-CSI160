# Working with user-defined functions
def test_function():
    pass  # A placeholder, so as to keep the interpreter from recognizing an error.


def PrintText():
    print("Here is some string")
    x = 1
    print("The value of x equals", x)
    y = 3
    z = x + y
    print(z)


x = 1  # Global Variable
y = 0
z = ""
def var_mgt():
    global x  # This is required because the function wants to change its value
    print("Here is some string")
    x = x + 1  # Local Variable, but is pulling the x to the right of the equal sign globally.
    print("The value of x equals", x)
    y2 = 3
    z2 = x + y2
    print("The value of z equals", z2)


# PrintText()  # This is a function call
var_mgt()  # Prints 5


def x_value():
    global x  # Use global first to avoid syntax issues.
    print(x)
    x = x - 1
    print(x)  # You do not have to declare global value here since you're calling the x value, but not changing it.


# x_value()  # Prints 2 (var_mgt redefined globally), and then 1 (x_value redefined globally)
