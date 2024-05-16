"""
A dictionary of grades and student names for a class.

ASSUMPTION: The data for this class is static and will NOT change

Authors: Savannah Ciak
Class: CSI-160-01
Assignment: Class Exercise 2
Due Date: 2 November 2023

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

grades = {'course': 'Intro to Programming', 'instructor': 'Dr Albert Einstein', 'Allen': 90,
          'Barbara': 92, 'Charles': 80, 'Denise': 85, 'Edward': 74, 'Frances': 80, 'Gary': 60,
          'Harry': 94, 'Janice': 91, 'Kelly': 84, 'Larry': 87}

# Adds the key and its value into a dictionary:
grades['Mary'] = 100
grades['Nancy'] = 64
grades['Olivia'] = 88
print('The information for Intro to Programming in Dictionary form is:', grades)
# ^Testing the addition to the dictionary

# 1. Separate the keys from the values to the lists 'student_names' and 'student_grades'
student_names = []
student_grades = []

for key in grades.keys():
    student_names.append(key)
student_names.remove('course')
student_names.remove('instructor')
for value in grades.values():
    student_grades.append(value)
student_grades.remove('Intro to Programming')
student_grades.remove('Dr Albert Einstein')

print('The student names are:', student_names)
print('The student grades are:', student_grades)

# 2. Count the number of students and output the results
count = 0
for i in student_names:
    count = count + 1
print("The total number of students in this class is:", count)

# 3. Determine the highest, lowest and the average grade in
# the class and output each of these results

student_grades.sort()  # Sorts so we can call highest and lowest indexes below
print('The highest grade in the class is:', student_grades[-1])
print('The lowest grade in the class is:', student_grades[0])
avg = sum(student_grades)/len(student_grades)  # Finds average of the grades
print('The average grade in the class is:', avg)

# 4. Find a way to create a new dictionary with all the students and their grades
# where the data is sorted from the highest grade to the lowest grade. Name this
# dictionary “grades_sorted”

course = grades['course']  # Saving the data before deleting it
instructor = grades['instructor']  # Saving the data before deleting it
del grades['course']  # Deleting so I can sort below
del grades['instructor']  # Deleting so I can sort below
grades_sorted = {}
grades_sorted = (dict(sorted(grades.items(), key=lambda item: item[1])))  # Sorted a dictionary by values
# print(grades_sorted)  # Testing the sort

# 5. Output the data from this dictionary (“grades_sorted”) where the string before the
# student’s name says “(student name) has a grade of” followed by the grade.

for i in grades_sorted:
    print(i, "has a grade of", str(value))  # Incomplete
    pass

# 6. Determine the student’s rank in the class. The student with the highest grade as a
# ranking of 1, the student with the next highest grade is ranked second in the class, etc.

# Incomplete

