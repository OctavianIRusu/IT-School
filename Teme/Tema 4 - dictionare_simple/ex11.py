# Creați un dicționar cu numele și notele a patru studenți.
# Afișați numele și media fiecărui student în ordine descrescătoare a mediei.

students = {"Sandu": [5, 4, 5], "George": [10, 9, 8], "Vasile": [5, 6, 7]}
std_means = {}

for k, v in students.items():
    std_means[k] = sum(v) / len(v)

for k, v in sorted(std_means.items(), key=lambda x: x[1]):
    print(k, v)