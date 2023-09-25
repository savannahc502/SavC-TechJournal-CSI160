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

print("The contents of new_list are:", new_list)
print(y)

# Pulling items from a list based on a negative index value
print("This is pulling from the -1 position", y[-2])  # Goes to the end of the list, pulls out the second item
                                                        # From the end of the list
print(myList[-2:1])  # Starting a slice with a negative values returns an empty list

names = ["john", "sally", "sam"]
names[2] = "chris"  # The value if "sam" was replaced by "chris"
print(names)
