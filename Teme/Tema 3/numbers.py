#Suma primelor n numere multiple de 3 si 5.

n = int(input("Valoare: "))

k = 0
c = 0
suma = 0

while k <= n:
    if c % 3 == 0 and c % 5 == 0:
        suma += c
        k += 1
    c += 1

print(suma)