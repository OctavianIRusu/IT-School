# Scrieti un program care sa ceara utilizatorului sa introduca un numar intreg, 
# iar apoi sa afiseze acel numar ridicat la puterea a doua. Daca utilizatorul 
# introduce un input invalid (de exemplu, un numar cu virgula), programul ar 
# trebui sa afiseze un mesaj corespunzator de eroare.

try:
    x = int(input("Introdu un numar intreg: "))
    result = x ** 2
    print("Rezultatul este:", result)
except ValueError:
    print("Input invalid! Introdu doar numere intregi.")