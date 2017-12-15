# Lab: Pig Latin
    ###### Delivery Method: Prompt Only
    #### Goal

    #Create a program asks for a _single_ English word and translates it to **Pig Latin**.
    #It prints out the input word and the resulting translation like the example below.

    #### Instructions

    #1. If the first letter is a consonant, move it to the end.
    #1. Add "ay" to the end of that.
    #1. If the first letter is a vowel, just ad "yay" to the end.

    #> Word? hat
    #> hat in Pig Latin is athay
    #> Word? apple
    #> apple in Pig Latin is appleyay


# PygLatin Converter Code
pyg = 'ay'
original = input('Enter a word: ')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first_letter = word[0]
    if first_letter == ('a' or 'e' or 'i' or 'o' or 'u'):
        new_word = word + pyg
        print (new_word)
    else:
        new_word = word[1:] + first_letter + pyg
        print (new_word)
else:
    print('empty')
