# Creați un dicționar cu numele și salariul a trei angajați.
# Afișați salariatul cu cel mai mare salariu.

employees = {
    "Radu": 3800,
    "Andreea": 4500,
    "Daniel": 6700
}

salariu_max = 0
nume_salariu_max = ""

for nume, salariu in employees.items():
    if salariu > salariu_max:
        salariu_max = salariu
        nume_salariu_max = nume

print(nume_salariu_max)