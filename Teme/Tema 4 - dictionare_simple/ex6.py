# Creați un dicționar cu numele și vârsta a trei persoane.
# Ștergeți persoana cu vârsta cea mai mică și afișați dicționarul actualizat.

persoane = {
    "Alin": 30,
    "Carla": 23,
    "George": 38
}

varsta_min = 1000
nume_varsta_min = ""

for nume, varsta in persoane.items():
    if varsta < varsta_min:
        varsta_min = varsta
        nume_varsta_min = nume

del persoane[nume_varsta_min]

print(persoane)