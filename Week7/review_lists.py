# Reviewing how to work with lists

numbers = [0, 1, 3, 5, 4, 2, 9, 6]
numbers.sort()
# print(numbers)
# x = numbers.median()
# print(x) #Returns a Traceback

list_sum = sum(numbers)  # Adds all the numbers in the list
list_min = min(numbers)  # Finds the minimum value in a list
list_max = max(numbers)  # Finds the maximum value in a list

# print(list_sum)
# print(list_min)
# print(list_max)

# A way to calculate the average of numbers in a list
# Average is to sum all values and then divide by the number of values in the list
list_avg = sum(numbers)/len(numbers)
# print("The average of the numbers in the list equals",list_avg)

letters = ['a', 'w', 'q', 'a', 's', 'd', 'c', 'z', 's']
# Develop code that will allow a user to input a letter. Search for the letter. Return its index position
# and how many times it was found in the list. If it is not in the list, let the user know it was not
# found in the list. Ask if the user would like to add it to the list. If yes, add it. If no, end.

user_letter = input("Please enter a lowercase letter of the English alphabet: ")

for index, i in enumerate(letters):
    count = 0
    if user_letter == i:
        count = count + 1
        print("The letter", user_letter, "was found at index", index)

if user_letter not in letters:
    user_append = input("Letter not found. Would you like to add the letter to the list? (yes/no):")
    if user_append == "yes":
        letters.append(user_letter)
        print("The list is now:", letters)
    else:
        print("Letter was not added to the list.")
