import random
card_values =  {'A':1, '02':2, '03':3, '04':4, '05':5, '6':6, '7':7, '8':8,
                  '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __repr__(self):
        return "{}{}".format(self.rank[0], self.suit[0])

deck = []


for s in suits:
    for rank, value in card_values.items():
        Card(s, rank, value)
        deck.append(Card(s, rank, value))

random.shuffle(deck)

print(deck)
print(deck.pop())

if ace in hand:
    if hand total + 10 <= 21:
        score = hand total + 10
    else:
        score
