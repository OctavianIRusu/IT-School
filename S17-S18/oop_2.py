from oop_new import Card, Deck

d1 = Deck()
d1.shuffle()
x_cards = d1.get_cards(10)

for i in x_cards:
    print(f"{i.number}{i.symbol}")

print(sum(x_cards))