user_info = {
    "first_name": "octavian",
    "last_name": "rusu",
    "address": "turda",
    "country": "ro"
}

USER_TEMPLATE = "Nume: {0} Prenume: {1} Country: {2}"

print(USER_TEMPLATE.format(
    user_info["last_name"], user_info["first_name"], user_info["country"]))
