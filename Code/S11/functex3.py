# Managerul de la fabrica de cutii are nevoie de un program care calculeaza pretul
# cutiilor in functie de dimensiunea si grosimea lor. Pentru o cutie cu volumul de 1000 de litri
# de gorsime 1, pretul este de 25 de lei.
# Pentru gorosimile 2 si 3, pretul creste cu 10 respectiv 20 la suta.
# Scrieti o functie care primeste 4 parametrii:
# - inaltimea cutiei
# - latimea cutiei
# - lungimea cutiei
# - tipul de carton (1, 2 sau 3)
# Functia returneaza pretul.

def box_price(height, width, length, thickness):
    volume = height * width * length
    if thickness == 1:
        return 25 * volume
    elif thickness == 2:
        return 25 * 1.1 * volume
    elif thickness == 3:
        return 25 * 1.2 * volume
    else:
        return "Nu exista acest tip de cutie."

print(f"Pretul cutiei: {box_price(1,1,1,4)}")