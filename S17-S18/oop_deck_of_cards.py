from typing import List, Self
import random

s1 = "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"

CARD_SYMBOLS = ["♠", "♥", "♦", "♣"]

CARD_VALUE_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "J": 12,
    "Q": 13,
    "K": 14
}


class Card:

    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number.")

        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol.")

        self.__number = number
        self.__symbol = symbol

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self) -> str:
        """trebuie sa returneze string"""
        return f"<{self.__number}{self.__symbol}>"

    def __repr__(self) -> str:
        return self.__str__()

    def get_value(self) -> int:
        return CARD_VALUE_MAP[self.__number]

    def get_symbol(self) -> str:
        return self.__symbol

    def __lt__(self, other: Self):
        return self.get_value() < other.get_value()

    def __le__(self, other: Self):
        return self.get_value() <= other.get_value()

    def __gt__(self, other: Self):
        return self.get_value() > other.get_value()

    def __ge__(self, other: Self):
        return self.get_value() >= other.get_value()

    def __eq__(self, other: Self):
        """ returneaza boolean, TRUE sau FALSE
        operator overloading (dam un anumit rol unui operator matematic)"""
        # if self.__number == other.__number:
        #     if self.__symbol == other.__symbol:
        #         return True
        # return False
        return self.get_value() == other.get_value()

    def __add__(self, other: Self):
        return self.__number + other.get_value()

    def __radd__(self, other) -> int:
        return other + self.get_value()

    # def __del__(self):
    #     """Destructor"""
    #     print("The card is deleted from memory.")


class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """

    def __init__(self) -> None:
        self.__cards = []
        for v in CARD_VALUE_MAP:
            for s in CARD_SYMBOLS:
                self.__cards.append(Card(v, s))

    def shuffle(self):
        return random.shuffle(self.__cards)

    def get_cards(self, num) -> List[Card]:
        """Return n cards."""
        list1 = []
        if num > len(self.__cards):
            raise ValueError("Insufficient cards in the deck.")
        for i in range(num):
            list1.append(self.__cards.pop())
        return list1

    def __str__(self) -> str:
        """trebuie sa returneze string"""
        return f"{self.__cards}"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self):
        """trebuie sa returneze int/float"""
        return len(self.__cards)


    def run_game(self):
        player_hand = self.get_cards(2)
        dealer_hand = self.get_cards(2)

        while True:
            if sum(player_hand) == 21:
                print("You win!")
                break
            elif sum(player_hand) < 21:
                try:
                    while 
"""fara try except - este raise error
    de folosit 2 variabile suma player si suma dealer in cod in loc de sum sum
"""