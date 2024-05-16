"""This module asks the user for several inputs, and the program responds as if it is "Barbie."
I hope you have a fabulous time talking with this Barbie Computer!

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 2 Lab: Conversation with a Computer
Due Date: 9/15/23

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

username = input("Hiya, Barbie! What's your name?")
# Asks for a string input and assigns it to the username variable.
print("I'm so excited to meet your amazing self,", username + "!")
# Replies back using the username variable's value.

print("")  # This line is added so the output has a blank space inbetween lines.

print("Say,", username + ",", "have you seen these new pair of rollerblades? We should go shoe shopping!")
# Reuses the username string input from earlier.
shoes_owned = int(input("How many pair of shoes do you own?"))
# Asks for an integer input and assigns it to the shoes_owned variable.
print("WOWSA.", shoes_owned, "shoes!")
# Prints the variable shoes_owned, which now has a value assigned to it.

shoes_total = (shoes_owned + 1)
# The line above created the new shoes_total variable.
print("That means after we buy these new rollerblades, you will own", shoes_total, "pairs of shoes!")
# Recalls the new variable shoes_total

print("")  # This line is added so the output has a blank space inbetween lines.

print("Rollerblades add 4 inches to my height in the new Barbie Movie.")
height_original = float(input("What's your height in inches?"))
# Asks for a float input and assigns it to the height_original variable.
print("Gee, us Barbie dolls are only 11.5 inches tall.", height_original, "is super tall to me!")
# Recalls the new variable height_original

print("")  # This line is added so the output has a blank space inbetween lines.

input("Do you think you're super tall?")
# Asks for an input that is not assigned to a variable.
print("Either way, you'll be a fabulous", height_original + 4, "inches tall when wearing your new kicks.")
# Recalls the height_original variable and adds 4 to its value.

rb_color = input("What color rollerblades are you going to buy?")
#  Asks for a string input and assigns it to the rb_color variable.

print("")  # This line is added so the output has a blank space inbetween lines.

print("OMG,", rb_color, "is such a gorgeous color! Maybe we should add sparkles to them later, so they shine like you!")
# Recalls the rb_color variable, which now has a value.
print("Sorry, Barbie", username+"--", "I gotta run to my Barbie Dream House party now. Toodaloo!")
# Ending line of program that recalls the first variable's, username, value.

"""
Works Cited: 
"Barbie." Wikipedia, Wikimedia Foundation, 8 Sept. 2023, en.wikipedia.org/wiki/Barbie. Accessed 14 Sept. 2023.
Above citation was used to find the average height of a Barbie Doll. 
"""
