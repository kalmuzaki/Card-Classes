from enum import Enum

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{0} of {1}".format(self.value.name,self.suit.name)

    def __gt__(self, other):
        if self.suit.value >= other.suit.value:
            if self.value.value > other.value.value:
                return True
        return False

    def __lt__(self, other):
        if self.suit.value <= other.suit.value:
            if self.value.value < other.value.value:
                return True
        return False

    def __eq__(self, other):
        if self.suit.value == other.suit.value:
            if self.value.value == other.value.value:
                return True
        return False

class Suit(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

class Value(Enum):
    ACE = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
