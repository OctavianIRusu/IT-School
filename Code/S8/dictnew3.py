students_grades = {
    "Ana": 9.5,
    "Ioan": 8.0,
    "Maria": 7.5,
    "Andrei": 9.0,
    "Elena": 10.0
}

print(students_grades["Ana"])       

print(students_grades.get("Ana"))   #get returneaza none daca nu gaseste cheia

print(students_grades.get("Ionut", "Studentul nu exista"))  # avantaj al utilizarii get fata de dict[]

nota = students_grades.get("Ionut")

if nota is not None:
    print(nota)
else:
    print("Studentul nu exista")