# Creați un dicționar cu numele și numărul de telefon a trei prieteni.
# Afișați numerele de telefon în ordine alfabetică a numelor.

agenda = {
    "Bogdan": "0726789654",
    "Paul": "0735879867",
    "Adi": "0757900856"
}

for nume in sorted(agenda):
    print(nume, agenda[nume])