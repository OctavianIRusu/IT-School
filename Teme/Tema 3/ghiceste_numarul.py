from random import randint

print("Incepe jocul!")

x = randint(1, 301)

guess = int(input("Introduceti un numar intre 1 si 300: "))
counter = 1

while guess != x:
    if abs(guess - x) >= 50:
        print("Gheata!")
    elif abs(guess - x) >= 40:
        print("Frig!")
    elif abs(guess - x) >= 30:
        print("Rece!")
    elif abs(guess - x) >= 20:
        print("Caldut!")
    elif abs(guess - x) >= 10:
        print("Cald!")
    elif abs(guess - x) >= 5:
        print("Frige!")
    elif abs(guess - x) >= 2:
        print("Arde!")
    guess = int(input("Introduceti alt numar intre 1 si 99: "))
    counter += 1
print(f"Ai avut nevoie de {counter} incercari pentru a ghici numarul: {guess}")
