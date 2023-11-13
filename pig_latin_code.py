# Working with character conversions - words and sentences

'''
ate = ateway is the pig latin translation
frog = rogfay is the pig latin translation
'''

vowels = ['a', 'e', 'i', 'o', 'u']

def convert_word(text):
    text = input('Input word:')
    if text[0].lower() in vowels:
        new_word = text + "way"
    else:
        new_word = text[1:] + text[0].lower() + 'ay'
    print(new_word)

def choose_process():
    print('Welcome to the pig latin translator.')
    print('Enter a "W" or w word translation or "S" for sentence translation:')
    choice = input()
    choice.upper()
    if choice == "W":
        chooseWord()
    else:
        chooseSentence()

def chooseWord():
    print('Please enter your word:')
    text = input()
    if text.isalpha:
        (convert_word(text))
    else:
        print('Invalid Input')
        choose_process()

def chooseSentence():
    print('Enter your sentence:')
    sentence = input()
    for i in sentence:
        if i.isaplha() == True or i.isspace() == True:
            continue
        else:
            print("Invalid data.")
            chooseSentence()