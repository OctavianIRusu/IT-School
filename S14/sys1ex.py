
# user_input = input("Introdu string: ")
# print(user_input[::-1])

import sys

if sys.version_info.major < 3:
    print(f"Versiunea {sys.version_info.major} nu este suportata.")

print("Hello!")

sys.exit()

print("Bye!")