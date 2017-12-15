import random

card_values = {
    'Ace': 1,
    '02': 2,
    '03': 3,
    '04': 4,
    '05': 5,
    '06': 6,
    '07': 7,
    '08': 8,
    '09': 9,
    '10': 10,
    'Jack': 10,
    'King': 10,
    'Queen': 10
}

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    # def __str__(self):
    #     return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank[0:], self.suit[0])

class Deck:
    def __init__(self):
        self.deck = []

        for s in suits:
            for rank, value in card_values.items():
                self.deck.append(Card(s, rank, value))
        # print (self.deck)

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck

    def cut_deck(self):
        i = random.randrange(len(self.deck))
        cut1 = self.deck[:i]
        cut2 = self.deck[i:]
        cut_deck = cut2 + cut1
        self.deck = cut_deck
        return self.deck

    def dealer_hand(self):
        card_dealt = self.deck.pop()
        return card_dealt
        # print (cut_deck)
        # player = [cut_deck.pop() for _ in range (2)]
        # print (player)

class Hand:
    def __init__(self):
        self.hand = []
        # self.player_hand = []
        # self.cpu_hand = []

    def hand_hit(self, deck_in_play):
        card_dealt = deck_in_play.dealer_hand()
        self.hand.append(card_dealt)
        return self.hand

    def __str__(self):
        return '{}'.format(self.hand)

    def __repr__(self):
        return self.__str__()

    # def player_hit(self):
    #     card_dealt = deck_in_play.dealer_hand()
    #     self.player_hand.append(card_dealt)
    #     return self.player_hand
    #
    # def cpu_hit(self):
    #     card_dealt = deck_in_play.dealer_hand()
    #     self.cpu_hand.append(card_dealt)
    #     return self.cpu_hand

class Game:
    pass

my_deck = Deck()
card = my_deck.dealer_hand()
# print (card)

player_hand = Hand()
# print (player_hand)
cpu_hand = Hand()
# print (cpu_hand)



player_hand.hand_hit(my_deck)
player_hand.hand_hit(my_deck)
print (player_hand.hand)


cpu_hand.hand_hit(my_deck)
cpu_hand.hand_hit(my_deck)
print (cpu_hand.hand)

player_total = []
cpu_total = []

for card in player_hand.hand:
    player_total.append(card.value)

for card in cpu_hand.hand:
    cpu_total.append(card.value)

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum(player_total))
print(listsum(cpu_total))




# player_hand = my_deck.dealer_hand()
# print (player_hand)
# cpu_hand = my_deck.dealer_hand()
# print (cpu_hand)
