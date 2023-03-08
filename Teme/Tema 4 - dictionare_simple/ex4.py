# Creați un dicționar cu numele și data de naștere a trei persoane.
# Adăugați o nouă persoană la dicționar și afișați numele și data de naștere a
# tuturor persoanelor.

persoane = {
    "Cosmin": "14.08.1980",
    "Laura": "8.03.1960",
    "Sergiu": "5.09.2000"
}

persoane["Relu"] = "30.06.1989"

for nume, data in persoane.items():
    print(nume, data)