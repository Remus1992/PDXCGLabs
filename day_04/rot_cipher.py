# Index     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
# English   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z
# ROT+13    n   o   p   q   r   s   t   u   v   w   x   y   z   a   b   c   d   e   f   g   h   i   j   k   l   m

# pre_code = input("Enter code: ")
# print (chr (65))
# print (ord ('A'))
# code_encrypted
# code_decrypted



#Caesar Cipher (from online)
MAX_KEY_SIZE = 26


def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)

        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))

# MikeyNON
# import time
# import string
# import codecs
# initial = input("Would you like to encrypt or decrypt?\n:")
# user_in = input("Message to Encrypt:\n")
# encryption_1 = codecs.encode(user_in, 'rot13')
# print("ENCRYPTING")
# time.sleep(3)
# print(encryption_1)

# # Rot 13 (my working version)
# def getMode():
#     while True:
#         print('Do you wish to encrypt or decrypt a message?')
#         mode = input().lower()
#         if mode in 'encrypt e decrypt d'.split():
#             return mode
#         else:
#             print('Enter either "encrypt" or "e" or "decrypt" or "d".')
#
# def getMessage():
#     print('Enter your message:')
#     return input()
#
# def getTranslatedMessage(mode, message):
#     key = 13
#     if mode[0] == 'd':
#         key = -key
#     translated = ''
#
#     for symbol in message:
#         if symbol.isalpha():
#             num = ord(symbol)
#             num += key
#
#             if symbol.isupper():
#                 if num > ord('Z'):
#                     num -= 26
#                 elif num < ord('A'):
#                     num += 26
#             elif symbol.islower():
#                 if num > ord('z'):
#                     num -= 26
#                 elif num < ord('a'):
#                     num += 26
#
#             translated += chr(num)
#
#         else:
#             translated += symbol
#     return translated
#
# mode = getMode()
# message = getMessage()
#
# print('Your translated text is:')
# print(getTranslatedMessage(mode, message))
