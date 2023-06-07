

def box_price(height, length, width, t):
    raw_price = height * length * width * 25
    if t == 1:
        return raw_price
    if t == 2:
        return raw_price * 1.1
    if t == 3:
        return raw_price * 1.2

    return -1

def get_offer_price(height, length, width, t, quantity):
    price_per_box = box_price(height, length, width, t)
    discount = quantity // 10
    price = price_per_box * quantity * ((100 - discount) / 100)

    return price



h = float(input("Inaltime cutie: "))
l = float(input("Lungime cutie: "))
w = float(input("Latime cutie: "))
q = float(input("Cantitate: "))


# print(box_price(1, 1, '1', 1))
print(f"Oferta pret: {get_offer_price(h, l, w, 1, q):.2f} RON")