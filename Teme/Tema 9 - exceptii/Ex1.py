# Scrieti un program care sa imparta doua numere intregi citite de la tastatura 
# si sa afiseze catul si restul. In cazul in care impartirea nu poate fi realizata 
# (de exemplu, in cazul in care al doilea numar este 0), programul ar trebui sa 
# afiseze un mesaj corespunzator de eroare.

a = int(input("Introdu primul numar: "))
b = int(input("Introdu al doilea numar: "))

try:
    cat = a // b
    rest = a % b
    print("Catul impartirii este:", cat)
    print("Restul impartirii este:", rest)
except ZeroDivisionError:
    print("Nu se poate imparti la zero!")

