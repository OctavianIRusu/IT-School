# Make a script which encrypts a string using Caesar cipher with key 20, use a 
# function to generate a dict representing the new alphabet

def get_alphabet(key):
    alphabet = {}
    for i in range(26):
        new_pos = (i + key) % 26
        old_char = chr(ord('A') + i)
        new_char = chr(ord('A') + new_pos)
        alphabet[old_char] = new_char
    return alphabet

def crypt(msj, key):
    alphabet = get_alphabet(key)
    encrypted = ""
    for char in msj:
        if char.isalpha():
            encrypted += alphabet[char.upper()]
        else:
            encrypted += char
    return encrypted

message = input("Enter your secret message: ")
key = int(input("Enter the key value between 1 and 25: "))
encrypted_message = crypt(message, key)
print("Encrypted message:", encrypted_message)