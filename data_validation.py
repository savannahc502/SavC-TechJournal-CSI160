var = "Here is some string data with the number two in it"
pswd = "asd213#!sd09"
num = 23423
num2 = '23423.468'
space = ' '
#print(len(pswd))
book = 'Why I Love To Program With Python'

'''
isupper() and islower()
'''
#name = 'ABC'
#print(name.isupper()) #If all characters are upper case, Python prints True

'''
String methods:
isalpha(): All alpha characters
isalnum(): Combination of alpha and numeric chars.
isdecimal(): Numeric values, not floating point values
isspace(): A space
istitle(): Each word begins with an upper case letter

print(var.isalpha())

print(space.isspace())
print(book.istitle())

print(str(num).isdecimal())
print(float(num2))
print(var.isalnum())
print(pswd.isalnum())

count = 0
for i in var:
  if(i.isalpha() == True or i.isspace() == True):
    continue
  else:
    count += 1
    print("Invalid data.")
    break
if(count == 0):
  print("The data passed validation.")
else:
  pass
  
#startswith() and endswith()
course = 'CSI-160'
if course.startswith('CSI') == True and course.endswith('160') == True:
  print("This is a valid course.")
else:
  print("Invalid course")
'''

'''
Password Validation:
1. 8 - 12 characters
2. at least one uppercase letter
3. at least one lowercase letter
4. at least one special character
5. at least one number
'''
def pswd_validator():
  chars = ['#', '!', '*', '%']
  upltr = False
  lowltr = False
  num = False
  special = False
  pswd = input('Input password')
  count = len(pswd)
  if count <8 or count >12:
    print('Please be sure to enter 8 to 12 characters')
    pswd_validator()
  else:
    for j in pswd:
      if j.isupper():
        upltr = True #Reassigns the variable a new value
      elif j.islower():
        lowltr = True
      elif j.isdecimal():
        num = True
      elif j in chars:
        special = True
      else:
        continue
  if upltr == True and lowltr == True and num == True and special == True:
    print("Valid password")
    exit()
  else:
    print("Process Failed")
    pswd_validator()

pswd_validator()

