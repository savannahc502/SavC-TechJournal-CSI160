""" This program uses a Game of Thrones character API to return a random
person from the book series, asks the user for some basic input on what
information they would like to see, and then returns if that person is one
of a few great fictional couples I have specified in the code.

OTP = One True Pairing
  - A nickname fans use when describing their favorite fictional couple

Author: Savannah Ciak
Class: CSI-160-01
Assignment: Week 12/13: JSON Programming Lab
Due Date: 1 December 2023

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

import requests
import random


# If statements to check for the best couple parings of GoT
def find_character_match(user_character_data):
    # Check if the user's character is Jon Snow
    if user_character_data['name'].lower() == 'jon snow':
        print("Your fandom OTP is Ygritte Styr!")
    # Check if the user's character is Ygritte Styr
    elif user_character_data['name'].lower() == 'ygritte styr':
        print("Your fandom OTP is Jon Snow!")
    # Check if the user's character is Jaime Lannister
    elif user_character_data['name'].lower() == 'jaime lannister':
        print("Your fandom OTP is Brienne of Tarth!")
    # Check if the user's character is Brienne of Tarth
    elif user_character_data['name'].lower() == 'brienne of tarth':
        print("Your fandom OTP is Lannister!")
    # Check if the user's character is Renly Baratheon
    elif user_character_data['name'].lower() == 'renly baratheon':
        print("Your fandom OTP is Loras Tyrell!")
    # Check if the user's character is Loras Tyrell
    elif user_character_data['name'].lower() == 'loras tyrell':
        print("Your fandom OTP is Renly Baratheon!")
    # Check if the user's character is Jorah Mormont
    elif user_character_data['name'].lower() == 'jorah mormont':
        print("Your fandom OTP is Daenerys Targaryen!")
    # Check if the user's character is Daenerys Targaryen
    elif user_character_data['name'].lower() == 'daenerys targaryen':
        print("Your fandom OTP is Jorah Mormont!")
    # Check if the user's character is Robb Stark
    elif user_character_data['name'].lower() == 'robb stark':
        print("Your fandom OTP is Theon Greyjoy!")
    # Check if the user's character is Theon Greyjoy
    elif user_character_data['name'].lower() == 'theon greyjoy':
        print("Your fandom OTP is Robb Stark!")
    else:
        print("No good romantic match found for the specified character.")


# Randomly picks one of the 582 GoT characters from the GoT API
def get_game_of_thrones_character():
    assignment = random.randint(0, 583)
    api_url = 'https://anapioficeandfire.com/api/characters/' + str(assignment)

    # GET request
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        character_data = response.json()
        return character_data
    else:  # Unique error code, given advice for this by Sierra Blume of Champlain College
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch data from the API (Status Code: {response.status_code})")
        return None


# Displays an option board for the user to pick what data they want to be given
def display_character_info(character_data):
    name = character_data['name']  # name
    if name == "":
        name = "N/A"
    culture = character_data['culture']  # culture
    if culture == "":
        culture = "N/A"
    born = character_data['born']  # born
    if born == "":
        born = "N/A"
    print(f'Your Random GoT Character is {name}. What would you like to know about them?')
    user_input = input(
        "Enter '1' for culture, '2' for their birth year, '3' for both, or anything else to terminate the code.")
    if user_input == '1':
        print(f"Culture: {culture}")
    elif user_input == '2':
        print(f"Born: {born}")
    elif user_input == '3':
        print(f"Culture: {culture}")
        print(f"Born: {born}")
    else:
        print("You must hate info then.")


# Starting Function
def main():
    # Uses get_game_of_thrones_character() function and assigns return value to got_character_data
    got_character_data = get_game_of_thrones_character()

    # Check if data retrieval was successful
    if got_character_data:
        display_character_info(got_character_data)
    else:
        exit()
    find_character_match(got_character_data)


main()  # Calls the starting function
