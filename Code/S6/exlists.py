alfabet = []

for i in range(65, 91):
    alfabet.append(chr(i))
print(alfabet)

alfabet.remove("H") # parcurge lista de la stanga la dreapta si elimina prima aparitie a acestei valori;
print(alfabet)


# eliminarea unei valori din toate aparitiile

temp = [33, 22, 34, 21, 22, 0]
to_remove = 22

while to_remove in temp:
    temp.remove(to_remove)
print(temp)

if 0 in temp:
    print("S-a produs inghet")

