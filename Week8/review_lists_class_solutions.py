# Class Code:
letters = ['a', 'w', 'q', 'a', 's', 'd', 'c', 'z', 's']


def find_ltr():
    ltr = input('Enter a letter:')
    count = 0
    for i in letters:
        if(i == ltr):
            count = count + 1
        else:
            continue
    print("The letter,", ltr, " was found", count, "times.")
    for idx, j in enumerate(letters):
        if j == ltr:
            print('The index position(s) of', ltr, "are:", idx)
        elif count == 0:
            print("Do you want to add the letter,", ltr, "to this list? (y/n")
            ans = input("Enter your response:")
            if ans == 'y':
                letters.append(ltr)
                print('The letter,', ltr, 'has been added to the list.')
                print(letters)
                exit()
            else:
                print('Good-bye')
                exit()
        else:
            continue


find_ltr()
