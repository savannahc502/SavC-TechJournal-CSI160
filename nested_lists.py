# Working with nested lists

number_sequence = [
    0, 1, 2, 3
]
# print(number_sequence)

# nested_num_list is an example of a nested list or a list within a list
nested_num_list = [
    [1, 2, 3],  # index position 0
    [4, 5, 6],  # index position 1
    [7, 8, 9],  # index position 2
    [0]
]
# print(nested_num_list[1])  # The interpreter treats nested lists in a row first, column second order.
# print(nested_num_list[1][2])  # Searches for the list row and prints from column 2

bad_nested_list = [['a', 'b'], ['z', 's', 'w'], ['q', 'e']]
good_nested_list = [
    ['a', 'b'],
    ['z', 's', 'w'],
    ['q', 'e']
]

'''
# Nested for loop to print every number in the nested_num_list on separate lines
for i in nested_num_list:  # This passes each nested list to i
    for j in i:  # This passes each individual item in a list to j
        print(j)
'''

new_list = []
for i in good_nested_list:
    for j in i:
        new_list.append(j)
new_list.sort()
print(new_list)

