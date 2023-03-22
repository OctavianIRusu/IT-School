# Write a function to set None at a specified key in a dict.

new_dict = { "Food": 250, "Rent": 350, "Car": 200}

def set_none_at_key(dictionary, key):
    dictionary[key] = None

set_none_at_key(new_dict, "Food")

print(new_dict)