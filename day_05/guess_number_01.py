# This is a guess the number game.
import random

guessesTaken = 0
number = random.randint(1, 1000000000)
print('I am thinking of a number between 1 and 1000000000.')

while guessesTaken < float ('inf'):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)









#
#
# # This is a guess the number game.
# import random
#
# guessesTaken = 0
# number = random.randint(1, 1000000000)
# print('I am thinking of a number between 1 and 1000000000.')
#
# # def guess_number ():
# #     guess = input()
# #     guess = int(guess)
# #     return guess
# #
# # def guess_check ():
# guess = input()
# guess = int(guess)
# print('Take a guess.')
#
# while guess!= number:
#     guessesTaken = guessesTaken + 1
#
#     if guess < number:
#         print('Your guess is too low.')
#         exit ()
#
#     if guess > number:
#         print('Your guess is too high.')
#         exit ()
#
#     if guess == number:
#         break
#
# if guess == number:
#     guessesTaken = str(guessesTaken)
#     print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
