# Make list of dictionaries, each dictionaries contains the following 
# attributes: name, age, gender; Read those info from keyboard input.

users = []  # Initialize an empty list to store dictionaries

# Prompt the user to input information for each person

while True:
    name = input("Enter name (or 'done' to finish): ")
    if name == 'done':
        break
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    users.append({'name': name, 'age': age, 'gender': gender})

# Sort the list by age
users_sorted = sorted(users, key=lambda user: user['age'])

# Print out the sorted list
print(users_sorted)

