# Introduction to dictionaries

course = {}  # Empty dictionary
courses = {'CSI-160':'Intro to Python', 'CSI-260':'Adv.Python', 'CSI-300':'Database Systems'}
# All keys in a dictionary must be unique. If not, data is overwritten.

# print(courses)
# print(courses.keys())
# print(courses.values())

# Using a loop to extract keys
for keys in courses.keys():
    pass
    # print(keys)

for values in courses.values():
    pass
    # print(values)

for key, value in courses.items():
    pass
    # print("The key is", key, "and the value is", value)

# A valid dictionary structure that includes a list
grades = {'CSI-160-01':'Intro to Python', 'Students':['John', 'Mary'], 'x':3}

'''
for i in courses:  # The default behavior of the interpreter is to search for keys
    if i == 'CSI-300':
        print("The course exists.", i)
    else:
        print('The key does not exist.')
'''

'''
for j in courses.values():
    if j == 'Database Systems':
        print("The course exists,", j)
    else:
        print("The key does not exist")
'''

def addToDictionary():
    for keys, values in courses.items():
        k = input("Key:")
        v = input("Value:")
        if k == "CSI-160" and v == "Intro to Python":
            print("The course exists.",)
            break
        else:
            print('The key does not exist.')


# addToDictionary()
# print(courses)
courses.update({'CSI-400':'A Great Course'})  # Adds a dictionary item to the dictionary
# print(courses)
courses.update({'CSI-400':'Software Engineering'})  # This updates the value of the key
# print(courses)
courses['CSI-140'] = 'More Engineering'  # Adds the key and its value into a dictionary
# print(courses)
courses['CSI-2600'] = 'Advanced Python'
print(courses)


del courses['CSI-2600']  # Deletes the entire item (key-value pairing) -- GONE FOREVER
# print(courses)
key = input('Enter the key to delete: ')
item = courses.pop(key)  # This will let you store a value, not a key, in a variable
print(item)
print(key)
print(courses)


# Restoring deleted data, provided you have properly stored it
courses[key] = item
print(courses)
print(dict(sorted(courses.items())))  # Sorts the dictionary by key

print(dict(sorted(courses.items(), key=lambda item: item[1])))  # Sorted a dictionary by values
