# Scrie un program care citeste de la tastatura doua numere,
# si calculeaza a / b daca a > b sau b / a daca a <= b. Afiseaza 
# rezultatul.

a = int(input("a = "))
b = int(input("b = "))

if a > b:
    print(a/b)
else:
    print(b/a)