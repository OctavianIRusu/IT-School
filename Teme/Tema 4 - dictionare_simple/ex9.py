# Creați un dicționar cu numele și nota a cinci studenți.
# Afișați numele studentului cu cea mai mare notă.

students_grades = {
    'Ana': 9.5,
    'Ioan': 8.0,
    'Maria': 7.5,
    'Andrei': 9.0,
    'Elena': 10.0
}

sorted_students = sorted(students_grades.items(), key=lambda x: x[1])
print(sorted_students[-1][0])