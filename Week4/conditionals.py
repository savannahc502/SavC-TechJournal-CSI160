# Working with conditional statements

def ChooseOne():
    x = int(input("Enter an integer value for x:"))
    #print("The original value of x equals", x)
    y = 2
    if(x == 0):
        print("The original value of x equals", x)
        x = x + 1
        print("The value of x equals", x)
    elif(y == 2):
        print("The value of 'y' equals", y)
    else:
        print("The condition failed, y = ", y)


# ChooseOne()

def MultiConditions():
    name = input("Enter your name:")
    print("Please enter 1, 2, 3, or 4 to the question below")  # Attempt to create clarity for the user.
    year = input("What year are you in at Champlain College?")
    if(name == "" or year == ""):  # Decide is an "and" or "or" is useful here
        print("Please enter you information")
    else:
        print("Welcome")

MultiConditions()
