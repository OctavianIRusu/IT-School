# Scrieti un program care sa ceara utilizatorului sa introduca doua numere,
# iar apoi sa afiseze suma lor. Daca utilizatorul introduce un input invalid 
# (de exemplu, un sir de caractere in loc de numere), programul ar trebui sa 
# afiseze un mesaj corespunzator de eroare.

try:
    a = int(input("a = "))
    b = int(input("b = "))
    suma = a + b
    print(f"Suma numerelor este {suma}")
except ValueError:
    print("Input invalid, introdu doar numere intregi.")