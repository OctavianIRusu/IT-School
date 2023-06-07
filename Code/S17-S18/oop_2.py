from oop_deck_of_cards import Card, Deck

d1 = Deck()
# d1.shuffle()
# x_cards = d1.get_cards(10)

# for i in x_cards:
#     print(f"{i.number}{i.symbol}")

# print(sum(x_cards))

d1_iter = iter(d1)

# for i in d1:
#     print(i)


def septica(deck: Deck):
    for card in deck:
        if card.get_value() >= 7:
            yield card


septica_cards = septica(d1)

d1.shuffle()

for i in septica_cards:
    print(i)
