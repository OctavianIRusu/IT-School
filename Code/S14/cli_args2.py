import sys

print("Hello!")

try:
    print(sys.argv[1] * int(sys.argv[2]))
except IndexError:
    print("Argumentul nu exista")
    sys.exit(1)
except ValueError:
    print("Tip argument incorect.")
    sys.exit(1)
print("Bye!")