# Working with conditionals and loops

mixedList = ["john", "sally", "sam", "Larry", "Mary", 1, 2, 6, 7, 9, 0, 2, 4, 5]
# mixed data types in a list are the bane of existence
title = "Python Programming"

# Review difference between data structures and data types

'''
mixedList.sort()
print(mixedList)  # This will not work because you cannot sort lists with different data types
'''


# Searching for an item in a list
def searchList():
    count = 0
    for i in mixedList:
        if(i == "sam"):
            count = count + 1
            item = i
        else:
            continue
    if(count == 0):
        print("The item was not found in the list")
    elif (count > 0):
        print("The item", item, "was found. It was found", count, "times.")
    else:
        print("Process failed, please try again.")


searchList()

'''
Data Validation:
isdigit() - Determines if a string value is an integer or not
isalpha() - Determines if a string value is composed of all alpha (letters) character
'''
def sortList():
    strings = []
    numbers = []
    strings = mixedList[0:5]
    numbers = mixedList[5:]
    print(numbers)
    print(strings)

sortList()
