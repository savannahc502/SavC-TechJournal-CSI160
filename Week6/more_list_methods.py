# Working with even more fun list methods

x = [1, 2, 5, 9, 4, 0, 3]
y = x  # Creates the list named 'y'
x.append(6)
x.append(7)
# Two new values appended to the list 'x'
print(y)  # But the list 'y' inherits those values

y.append('string')
print(x)  # Data integrity FAILS!!

x = tuple(x)  # Converts the list 'x' into a tuple
print(x)
print(y)

a1 = [1, 2, 3, 4]
a2 = tuple(a1)

print(a1)
print(a2)
