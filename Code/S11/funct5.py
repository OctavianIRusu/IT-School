

def box_price(height, length, width, thickness):

# verificari - pentru a ne asigura ca output-ul functiei este de tipul pe care ni-l dorim

    if not isinstance(height, float):
        return 0
    
    if not isinstance(length, float):
        return 0
    
    if not isinstance(width, float):
        return 0
    
    raw_price = height * length * width * 25
    return raw_price

# float face deja verificare daca ce a introdus user-ul poate fi convertit in float

h = float(input("Inaltime cutie: "))
l = float(input("Lungime cutie: "))
w = float(input("Latime cutie: "))

print(f"Pret cutie 1x1x1 este: {box_price(h, l, w, 1):.2f} RON.")