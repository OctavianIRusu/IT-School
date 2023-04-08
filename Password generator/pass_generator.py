import string
import random


def get_user_length() -> int:
    """
    Prompts the user to input the length of the password and returns it as an integer.
    Raises a ValueError if the user's input is not an integer.
    """
    length = input("Password length: ")
    try:
        return int(length)
    except:
        raise ValueError("Not an integer!")


def get_user_choice(prompt: str) -> bool:
    """
    Prompts the user with a yes/no question to let the user choose if the
    password should contain digits or symbols. Returns a boolean value.
    """
    while True:
        choice = input(prompt)
        if choice.lower() not in ("y", "n"):
            print("Not an appropriate choice: choose between y and n!")
        else:
            return choice.lower() == "y"


def create_password():
    """
    Generates a password based on the user's chosen length and character sets.
    Prints the password to the console.
    """
    password = ""
    last_char = ""
    user_chars = string.ascii_letters
    if digit:
        user_chars += string.digits
    if symbol:
        user_chars += string.punctuation
    while len(password) < pass_length:
        c = user_chars[random.randint(0, len(user_chars)-1)]
        if c != last_char:
            password += c
            last_char = c
    return print(password)


pass_length = get_user_length()
digit = get_user_choice("Use digits [y/n]? ")
symbol = get_user_choice("Use symbols [y/n]? ")

create_password()
