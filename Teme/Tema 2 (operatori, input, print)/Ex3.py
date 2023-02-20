# Scrie un program care citeste de la tastatura doua numere, a si b.
# Daca a > b sa se calculeze diferenta si suma lor.
# Daca a == b sa se afiseze a la puterea b.
# Altfel sa se afiseze suma lor.

a = int(input("Introduceti o valoare pentru a: "))
b = int(input("Introduceti o valoare pentru b: "))

if a > b:
    print("Diferenta este " + str(a-b))
    print("Suma este " + str(a+b))
elif a == b:
    print("Rezultatul ridicarii la putere este " + str(a**b))
else:
    print("Suma este " + str(a+b))