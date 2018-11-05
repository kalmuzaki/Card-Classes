from Card import *
from random import randrange

class Deck:

    def __init__(self):
        self.cards = []

        for s in Suit:
            for v in Value:
                self.cards.append(Card(s,v))

    def shuffle(self):
        shuffledDeck = []

        #Shuffle all but the last remaining card
        while len(self.cards) > 1:
            selector = randrange(1,len(self.cards)) - 1
            shuffledDeck.append(self.cards.pop(selector))

        #put the last remaining card into the shuffled deck
        shuffledDeck.append(self.cards.pop(0))

        self.cards = shuffledDeck

    def deal_one_card(self):
        try:
            return self.cards.pop(0)
        except:
            return None
