#Sa se afiseze suma multiplilor de 5 din intervalul 0 - 1000

ran = range(0, 1001, 5)

suma = 0

for i in ran:
    suma = suma + i

print(suma)