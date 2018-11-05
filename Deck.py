from Card import *

class Deck:

    def __init__(self):
        self.cards = []

        for s in Suit:
            for v in Value:
                self.cards.append(Card(s,v))

    #def shuffle(self):

    #def deal_one_card(self):
