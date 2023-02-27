elev = ("Rusu Octavian", 9)

print(elev[0], "media la informatica", elev[1])

# Metoda 1

# nume_elev = elev[0]
# nota_elev = elev[1]

# Metoda 2 - tuple unpacking - da eroare daca avem elemente mai putine sau mai multe decat cele stocate in tuple

nume_elev, nota_elev = elev
print(nume_elev)
print(nota_elev)

# Metoda 3
nume_elev, *others = elev       # primul element este stocat separat, restul sunt stocate in lista