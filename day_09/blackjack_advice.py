def advise_blackjack(c):
    hand = c
    if hand <= 15:
        print ("Hit")

    if hand > 15 and hand < 21:
        print ("Stay")

    if hand == 21:
        print ("BlackJack!")

    if hand > 21:
        print ("You lost. Sorry :( ")

# cards = 10 + 5
# advise_blackjack(cards)

value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '0':10, 'J':10, 'Q':10, 'K':10, 'A':1}

hand_entered = input("Enter cards wih a comma and a space: ").replace(' ','').split(',')
print (hand_entered)
# print (*hand_entered)

for x in range(len(hand_entered)):
    hand_entered[x] = value.get(hand_entered[x])

print (hand_entered)

sum_hand = sum (hand_entered)

print (sum_hand)

advise_blackjack(sum_hand)
