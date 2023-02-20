# Scrie un program care citeste de la tastatura un numar 
# natural pozitiv din 3 cifre. Daca numarul introdus nu are 3 cifre sau 
# este un numar negativ se afiseaza: "Eroare".
# Daca ultima cifra din numarul introdus este mai mare sau egala cu 5,
# se va afisa suma dintre numarul introdus si ultima sa cifra, altfel 
# se va afisa diferenta dintre numarul introdus si ultima sa cifra.

num = int(input("Introdu un numar natural pozitiv format din 3 cifre: "))

if num < 0 or num < 100 or num > 999:
    print("Eroare")
elif num % 10 >= 5:
    print(num + num % 10)
elif num % 10 < 5:
    print(num - num % 10)