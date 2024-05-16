# Working with Lists

x = []  # Empty list

x = ['a', 'b', 3, True]
# print(x)
# print(x[1])
# print(x[8]) Creates a traceback because there is no value in this index

# Working with the 'for' loop
for i in x:  # The 'i' is a variable. The loop will pass a value from the list 'x' to 'i'
    print(i)  # Prints the current value of 'i'


length = len(x)
# print(length)

myList = [1, 2, 6, 7, 9, 0, 2, 4, 5]
new_list = x + myList  # List Concatenation
# print(new_list)

y = new_list[4:5]  # Asks for a range of output. The output starts with the value in the
                    # second index position. It includes all values up to BUT DOES NOT INCLUDE
                    # the value of the last index position. This is called a 'slice'.

# print("The contents of new_list are:", new_list)
# print(y)

# Pulling items from a list based on a negative index value
# print("This is pulling from the -1 position", y[-2])  # Goes to the end of the list, pulls out the second item
                                                        # From the end of the list
# print(myList[-2:1])  # Starting a slice with a negative values returns an empty list

names = ["john", "sally", "sam", "Larry", "Mary"]
names[2] = "chris"  # The value if "sam" was replaced by "chris"
# print(names)

pos = names.index('chris')  # The index method returns the index position of a value in the list
print(pos)

names.remove("chris")  # The remove() will remove an item named in the function. The value
                        # of 'chris' is gone. You cannot pass the value you removed to a variable.
                        # Pass the value to a variable before it is removed.
print(names)

del myList[4]  # Deletes the item according to the index position noted.
print(myList)

names.append('sam')  # Adds the value in the () to the end of the specified list
print(names)

names.insert(10, 'keith')  # This inserts a value at a specific index position in the list. The first value
                          # must be the index position and the second value is the item.
                          # This will not override values, but instead push them out further
print(names)
pos1 = names.index('keith')
print(pos1)  # This proves that if you ask for a variable to be added or inserted past the max of the list,
                # python interpreter will add it to the end of the list.

print(myList)  # This shows the items as they are in the list
myList.sort()
print(myList)  # This shows the sorted list

print(names)
names.sort()  # capitalized words take precedent over lowercase when sorted
print(names)
names.sort(reverse=True)  # performs a reverse sort
print(names)

names.sort(key=str.lower)  # sorts by strict alphabetic rules (no capitalization preference)
print(names)

mixedList = ["john", "sally", "sam", "Larry", "Mary", '1', '2']
mixedList.sort()  # String numbers get sorted first followed by capitalized names followed by lowercase names
print(mixedList)
