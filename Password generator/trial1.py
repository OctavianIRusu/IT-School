import string
import random

"""Defining the constants that return the chosen type of characters"""
letters = string.ascii_letters
letters_num = letters + string.digits
letters_symb = letters + string.punctuation
all_char = letters + string.digits + string.punctuation


length = input("Password length: ")

while True:
    use_digits = input("Use digits [y/n]? ")
    if use_digits.lower() not in ("y", "n"):
        print("Not an appropriate choice: choose between y and n!")
    else:
        break

while True:
    use_symbols = input("Use symbols [y/n]? ")
    if use_symbols.lower() not in ("y", "n"):
        print("Not an appropriate choice: choose between y and n!")
    else:
        break

def get_user_length():
    try:
        return int(length)
    except:
        raise ValueError("Insert an integer!")

def get_user_use_digits():
    if use_digits == "y":
        return True
    if use_digits == "n":
        return False

def get_user_use_symbols():
    if use_symbols == "y":
        return True
    if use_symbols == "n":
        return False
    
def create_password():
    password = list()
    for i in range(get_user_length(length)):
        if get_user_use_digits(use_digits) and get_user_use_symbols(use_symbols):
            password.append(all_char[random.randint(0, len(all_char) + 1)])
        elif get_user_use_digits(use_digits) and not get_user_use_symbols(use_symbols):
            password.append(letters_num[random.randint(0, len(letters_num) + 1)])
        elif get_user_use_symbols(use_symbols) and not get_user_use_digits(use_digits):
            password.append(letters_symb[random.randint(0, len(letters_symb) + 1)])
        else:
            password.append(letters[random.randint(0, len(letters))])
    str_password = "".join(password)
    return print(str_password)

create_password()