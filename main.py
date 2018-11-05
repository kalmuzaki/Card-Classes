import importlib
from Card import *
from Deck import *

cardsOnTheTable = [] #the cards that are on the table

#first we get a new deck
myDeck = Deck()

#then we shuffle the cards
myDeck.shuffle()

#then we deal them all out
for i in range(1, 60):
    myCard = myDeck.deal_one_card()
    if isinstance(myCard, Card):
        cardsOnTheTable.append(myCard)

#what do we now have on the table?
for c in cardsOnTheTable:
    print(c)
