# Working with try... except

def calc_reciprocal():
    try:
        x = int(input('Enter a number:'))
        z = 1/x
        print(z)
        
    except Exception as e:
        print("There was an error in the calculation:", e)
        calc_reciprocal()
calc_reciprocal()
