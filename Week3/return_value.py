# Using 'return' in a function

def calc1():
    x = 1
    y = 2
    z = x + y
    print("This is from the calc1 function:", z)


def calc2():
    x = 5
    y = 2
    z = x * y
    return z  # The result of the operation is held in memory. The function call results in
                # in the ANSWER becoming available for use.


calc1()
print("This is from the calc2 function:", calc2())
