# Parametri optionali (prestabiliti)
def box_price(height, length, width, t=1, price=25, **kwargs):
    """ Calculate the box price.
    kwargs:
        - cq2: coefficient for type 2
        - cq3: coefficient for type 3
    """
    raw_price = height * length * width * price
    if t == 1:
        return raw_price
    if t == 2:
        return raw_price * kwargs.get("cq2", 1.1)
    if t == 3:
        return raw_price * kwargs.get("cq3", 1.2)
    
print(box_price(1, 2, 3, t=2, cq2=2, x=3))

# Functii care primesc perechi chei-valoare
def demo(**kwargs):
    print(kwargs)

demo(a=3, b=3, alex=32, new="test")