# Creați un dicționar cu numele și nota a patru studenți. Adăugați o
# nouă intrare în dicționar pentru un nou student și actualizați nota unui 
# student existent. Afișați numele studenților si nota in ordine alfabetică.

elevi = {
    "Andrei": 8,
    "Oana": 10,
    "Matei": 6.7,
    "Sergiu": 8.7
}

elevi["Sorin"] = 6.8
elevi["Oana"] = 9.6

for k, v in sorted(elevi.items()):
    print(k, v)