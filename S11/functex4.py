# Scrieti o functie care genereaza o oferta de pret pentru managerul de la fabrica 
# de cutii. Functia trebuie sa aplice un discount de cantitate. Pentru fiecare 100 de cutii se
# aplica 1% reducere. Functia primeste toti parametrii necesari pentru calculul pretului cutiei si
# inca un parametru care reprezinta numarul de cutii.

def box_price(height, length, width, thickness):
    raw_price = height * length * width * 25
    if thickness == 1:
        return raw_price
    elif thickness == 2:
        return raw_price * 1.1
    elif thickness == 3:
        return raw_price * 1.2
    else:
        return -1

def get_offer_price(height, length, width, thickness, quantity):
    price_per_box = box_price(height, length, width, thickness)
    discount = quantity // 100
    price = price_per_box * quantity * ((100 - discount) / 100)

    return price


h = float(input("Inaltime cutie: "))
l = float(input("Lungime cutie: "))
w = float(input("Latime cutie: "))
q = float(input("Cantitate: "))

print(f"Oferta pret: {get_offer_price(h, l, w, 1, q):.2f} RON.")