students_grades = {
    "Ana": 9.5,
    "Ioan": 8.0,
    "Maria": 7.5,
    "Andrei": 9.0,
    "Elena": 10.0
}

lista_chei = students_grades.keys()

for name in lista_chei:
    print(name)

print("-"*30)

for value in students_grades.values():
    print(value)

print("-"*30) 

valori = students_grades.items()

for v in valori:
    name, grade = v
    print(name, grade)

print("-"*30) 

for k, v in students_grades.items():
    print(k, v)