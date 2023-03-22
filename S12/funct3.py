def box_price(h, l, w, type=1, p=25, **kwargs):
    """ Calculate the box price.
    kwargs:
        - cq2: coefficient for type 2
        - cq3: coefficient for type 3
    """
    raw_price = h * l * w * p
    if type == 1:
        return raw_price
    if type == 2:
        return raw_price * kwargs.get("cq2", 1.1)
    if type == 3:
        return raw_price * kwargs.get("cq3", 1.2)

boxes = [
    {
    "h": 2,
    "l": 3,
    "w": 4
    },
    {
    "h": 2,
    "l": 3,
    "w": 4,
    "type": 2
    },
    {
    "h": 2,
    "l": 3,
    "w": 4,
    "type": 2,
    "p": 23
    }
]

# for box in boxes:
#     if "p" in box:
#         print(f"Pret cutie: {box_price(box['h'], box['l'], box['w'], box['type'], box['p'])} RON")
#     elif "type" in box:
#         print(f"Pret cutie: {box_price(box['h'], box['l'], box['w'], box['type'])} RON")
#     else:
#         print(f"Pret cutie: {box_price(box['h'], box['l'], box['w'])} RON")

for box in boxes:
    print(f"Pret cutie: {box_price(**box)} RON")