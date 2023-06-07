sum = float(input("Introduceti suma: "))
TVA = 0.19

tva_calc = sum * TVA
total = sum + tva_calc

print("TVA-ul este " + str(tva_calc))
print("Suma totala este " + str(total))