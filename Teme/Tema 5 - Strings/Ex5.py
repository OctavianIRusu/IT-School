# Extract the number from import_numbers variable.

import_numbers = "Today we had 280 clients."

for i in import_numbers.split(" "):
    if i.isnumeric():
        print(i)