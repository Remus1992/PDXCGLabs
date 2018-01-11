import random

card_values = {
    'Ace': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6,
    '07': 7, '08': 8, '09': 9, '10': 10, 'Jack': 10, 'King': 10,
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

    def cut_deck(self):
        i = random.randrange(len(self.deck))
        cut1 = self.deck[:i]
        cut2 = self.deck[i:]
        cut_deck = cut2 + cut1
        self.deck = cut_deck

    def dealer_hand(self):
        card_dealt = self.deck.pop()
        return card_dealt
        # print (cut_deck)
        # player = [cut_deck.pop() for _ in range (2)]
        # print (player)

class Hand:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0

    def hand_hit(self, deck_in_play):
        card_dealt = deck_in_play.dealer_hand()
        self.hand.append(card_dealt)
        return self.hand

    def score_hand(self):
        self.value = 0
        for card in self.hand:
            self.value += card.value

    def __str__(self):
        return '{}'.format(self.hand)

    def __repr__(self):
        return self.__str__()

class Game:
    def __init__(self):
        self.my_deck = Deck()
        self.my_deck.shuffle_deck()
        self.my_deck.cut_deck()

        self.card = self.my_deck.dealer_hand() #just serves to remove a single card
        # print (card)

        self.player_hand = Hand("Player")
        self.cpu_hand = Hand("Dealer")

        self.initial_hand(self.player_hand)
        self.initial_hand(self.cpu_hand)

    def initial_hand(self, who):
        who.hand_hit(self.my_deck)
        who.hand_hit(self.my_deck)
        if who == self.player_hand:
            print("{} Hand: {}".format(who.name, who.hand))
            who.score_hand()
            # print (who.value)
        elif who == self.cpu_hand:
            print("{} Hand: X, {}".format(who.name, who.hand[1]))
            who.score_hand()
            # print (who.value)

    def stay_hit(self, who, option):
        if option == "hit":
            who.hand_hit(self.my_deck)
            who.score_hand()
            print("Player Hand: ", who.hand) #maybe need to wrap'
            # print (who.value)

        elif option == "stay":
            who.score_hand()
            print("Player Hand: ", who.hand)
            # print (who.value)

        else:
            print ("Player Error")

    def cpu_stay_hit(self, who, option):
        if option == "hit":
            who.hand_hit(self.my_deck)
            who.score_hand()
            print("Dealer Hand: ", who.hand)

        elif option == "stay":
            who.score_hand()
            print("Dealer Hand: ", who.hand)

        else:
            print ("Dealer Error")

    def check_game(self):
        if 21 >= self.player_hand.value > self.cpu_hand.value:
            print("Player Wins!")
        elif 21 >= self.cpu_hand.value > self.player_hand.value:
            print("Dealer Wins!")
        else:
            print("Draw Game!")

    def game_play(self):
        while True:
            if self.player_hand.value > 21:
                print ("Bust!")
                break
            elif self.player_hand.value == 21:
                print ("Winner!")
                break
            elif self.player_hand.value <21:
                query = input("Would you like to stay or hit?:\n")
                self.stay_hit(self.player_hand, query)
                if query == "stay":
                    break

        while True:
            if self.cpu_hand.value > 21:
                print ("Dealer Bust! You Win!")
                break
            elif self.cpu_hand.value == 21:
                print ("Dealer Wins! You Lose!")
                break
            elif self.cpu_hand.value < 15:
                self.cpu_stay_hit(self.cpu_hand, "hit")
            elif self.cpu_hand.value >= 15:
                self.cpu_stay_hit(self.cpu_hand, "stay")
                break

        self.check_game()

game = Game()
game.game_play()

"""
    def adjust_ace_value(self):
        global deck
        total_of_non_ace_cards = sum(deck.values_lookup[i] for i in self.cards if i != 'A')
        if total_of_non_ace_cards <= 10:
            self.values[self.cards.index('A')]=11
        else:
            self.values[self.cards.index('A')]=1
"""
