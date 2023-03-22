# Scrieti un program care sa ceara utilizatorului sa introduca o lista de numere 
# intregi separate prin virgula, iar apoi sa afiseze suma lor. In cazul in care 
# inputul utilizatorului este invalid, programul ar trebui sa afiseze un mesaj 
# corespunzator de eroare.

try:
    numere = input("Introdu o lista de numere intregi separate prin virgula: ")
    num_list = [int(x) for x in numere.split(",")]
    result = sum(num_list)
    print(f"Suma numerelor este: {result}")
except ValueError:
    print("Input invalid! Introdu numere intregi separate prin virgula.")