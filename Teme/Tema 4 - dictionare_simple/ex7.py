# Creați un dicționar cu numele și ocupația a cinci persoane.
# Apoi utilizați o buclă "for" pentru a itera prin dicționar și afișați numele
# și ocupația fiecărei persoane.

dict = {
    "Carla": "Analist",
    "Alexandra": "Manager",
    "Marius": "Economist",
    "Sergiu": "Actor",
    "Sara": "Fotograf"
}

for nume, ocupatie in dict.items():
    print(nume, "-", ocupatie)