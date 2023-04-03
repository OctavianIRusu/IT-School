from typing import List, Self

s1 = "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"

class Card:

    def __init__(self, number: int, symbol: str) -> None:
        self.__number = number
        self.__symbol = symbol
    
    def __str__(self) -> str:
        """trebuie sa returneze string"""
        return f"<{self.__number}{self.__symbol}>"

    def __repr__(self) -> str:
        return self.__str__()

    def get_number(self) -> int:
        return self.__number
    
    def get_symbol(self) -> str:
        return self.__symbol

    def __lt__(self, other: Self):
        return self.__number < other.get_number()
    
    def __le__(self, other: Self):
        return self.__number <= other.get_number()

    def __gt__(self, other: Self):
        return self.__number > other.get_number()
    
    def __ge__(self, other: Self):
        return self.__number >= other.get_number()

    def __eq__(self, other: Self):
        """ returneaza boolean, TRUE sau FALSE
        operator overloading (dam un anumit rol unui operator matematic)"""
        # if self.__number == other.__number:
        #     if self.__symbol == other.__symbol:
        #         return True
        # return False
        return self.__number == other.get_number()

    def __add__(self, other: Self):
        return self.__number + other.get_number()

class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """
    def __init__(self) -> None:
        self.__cards = []

    def __len__(self):
        """trebuie sa returneze int/float"""
        return len(self.__cards)

d1 = Deck()

print(f"Cards in deck: len(d1)")

c1 = Card(2, s1)
c2 = Card(3, s1)

print(c1 + c2)