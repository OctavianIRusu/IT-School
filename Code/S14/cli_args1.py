import sys

print("Hello!")

try:
    print(sys.argv[1][::-1])
except IndexError:
    print("Argumentul nu exista")
    sys.exit(1)

print("Bye!")