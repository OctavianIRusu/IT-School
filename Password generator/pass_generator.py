import string
import random


def get_user_length() -> int:
    """
    Prompts the user to input the length of the password and returns it as an integer.
    """
    while True:
        length = input("Password length: ")
        if int(length) <= 0:
            print("The length cannot be negative or zero.")
        else:
            return int(length)


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


def create_password(pass_length: int, digit: bool, symbol: bool) -> str:
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
    return password


try:
    print(create_password(get_user_length(), get_user_choice(
        "Digit y/n?"), get_user_choice("Symbol y/n?")))
except:
    raise ValueError("The input is not an integer!")
