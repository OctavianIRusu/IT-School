# Creați o listă cu patru tuple, fiecare tuplă conținând numele
# și vârsta unui angajat. Convertiți lista într-un dicționar unde
# cheia este numele angajatului și valoarea este vârsta acestuia.

empl = [("Ana", 25), ("Ioan", 32), ("Maria", 41), ("Andrei", 19)]

empl_dict = {}

for i in empl:
    empl_dict[i[0]] = i[1]

print(empl_dict)