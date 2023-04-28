n = int(input("Introduceti un numar natural pozitiv: "))

fact = 1

if n < 0:
    print("Alegeti un numar pozitiv!")
if n == 0:
    print(f"{n}! = 1")
if n == 1:
    print(f"{n}! = 0")
else:
    for i in range(2, n + 1):
        fact *= i
    print(f"{n}! = {fact}")
