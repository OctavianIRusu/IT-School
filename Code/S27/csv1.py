# csv = comma separated values

import csv

with open("salarii.csv") as fin:
    reader = csv.reader(fin.readlines())
for line in reader:
    print(
        f"Full name: {line[0]} {line[1]} | Net salary: {float(line[-2]) * 0.45}")

with open("salarii.csv") as fin:
    reader = csv.DictReader(fin.readlines())
for line in reader:
    print(f"Salariu brut: {line["salariu"]}")

# de creat un csv nou doar cu coloanele nume, prenume si salariu net

with open("salarii_nete.csv", "w") as fout:
    writer = csv.writer(fout)
    for line in reader:
        writer.writerow([line[0], line[1]])