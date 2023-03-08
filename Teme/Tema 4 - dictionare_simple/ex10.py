# Creați un dicționar cu numele și vârsta a patru persoane.
# Sortați dicționarul în funcție de vârstă și afișați numele și vârsta
# fiecărei persoane în ordine crescătoare de vârstă.

contacts_ages = {
    'Ana': 25,
    'Ioan': 32,
    'Maria': 41,
    'Andrei': 19
}

for k, v in sorted(contacts_ages.items(), key=lambda x: x[1]):
    print(k, v)