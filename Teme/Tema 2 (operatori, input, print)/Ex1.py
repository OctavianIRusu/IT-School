# Scrie un program care citeste de la tastatura un numar 
# natural si afiseaza "Par" daca numarul este par sau "Impar" 
# daca numarul este impar.

number = int(input("Introduceti numarul: "))

if(number % 2) == 0:
    print("Numarul introdus este par.")
else:
    print("Numarul introdus este impar.")