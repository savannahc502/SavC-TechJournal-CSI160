# Reviewing how to work with functions

def tryAgain():
    print("The process is finished, data saved.")
    x = input('Do you want to add another account? (y/n)')
    if x == "y":
        get_info()
    else:
        print("Good-bye")
        exit()


def get_info():
    name = input("Enter username here: ")
    pswd = input("Enter your password: ")
    bank_acct = input("What is your bank account number?")
    showData(name, pswd, bank_acct)


customer = []


def showData(name, pswd, bank_acct):
    print("Hello,", name + ".", "Thank you for your information.")
    print("We are adding your information to our dataset.")
    customer.append([name, pswd, bank_acct])
    print("Please confirm we have the correct data.")
    '''
        Creates a simple list
        customer.append(name)
        customer.append(pswd)
        customer.append(bank_acct)
    '''
    save_customer_datab = tuple(customer)
    print("Your full name:", name)
    print("Your password:", pswd)
    print("Bank account number:", bank_acct)
    print(customer)
    print(save_customer_datab)
    tryAgain()

get_info()
