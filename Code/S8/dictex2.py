catalog = {
    "Cosmin": [5, 7, 10],
    "Adrian": [6, 8, 9],
    "Mara": [4, 7, 8]
}

for elev in catalog.keys():
    print(elev, sum(catalog[elev])/len(catalog[elev]))

print("-"*30)

for nume, nota in catalog.items():
    media = sum(nota)/len(nota)
    print(nume, media)
    