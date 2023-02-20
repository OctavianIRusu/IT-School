# Scrie un program care citeste de la tastatura un numar 
# natural, reprezentand raza unui cerc, si afiseaza perimetrul
# cercului insotit de mesajul "Perimetru cercului = <valoare>".
# Daca numarul citit este mai mare decat 100 se va calcula si aria
# cercului. Aceasta se va afisa insotita de mesajul "Aria cercului = <valoare>".

radius = int(input("Introdu raza cercului: "))
PI = 3.14

if radius <= 0:
    print("Introdu un numar natural, mai mare decat 0!")
else:
    print("Perimetrul cercului = " + str(2*PI*radius))

if radius > 100:
    print("Aria cercului = " + str(PI*radius**2))