import random
import time
guess_count = 0
print("\n\nI'm going to guess the number youre thinking of!\n")
m = 0
mx = 3000
not_guessed = True
while not_guessed and guess_count < 4:
    guess_count += 1
    comp_num = random.randint(m,mx)
    print(comp_num)
    time.sleep(1)
    user_guess = input("Did I guess (c)orrectly, (h)igh or (l)ow?: ")
    if user_guess == 'h':
        mx = comp_num
    elif user_guess == 'l':
        m = comp_num
    elif user_guess == 'c' and guess_count == 1:
        print("I'm a genius.")
        exit()
    elif user_guess == 'c':
        print('Awesome, I guessed in {} guesses'.format(guess_count))
        exit()
    else:
        print('I don\'t understand')
else:
    print('I didn\'t get it in time.')
