# def print_menu():
#     print('1. Print Phone Numbers')
#     print('2. Add a Phone Number')
#     print('3. Remove a Phone Number')
#     print('4. Lookup a Phone Number')
#     print('5. Quit')
#     print()
#
# numbers = {}
# menu_choice = 0
# print_menu()
# while menu_choice != 5:
#     menu_choice = int(input("Type in a number (1-5): "))
#     if menu_choice == 1:
#         print("Telephone Numbers:")
#         for x in numbers.keys():
#             print("Name: ", x, "\tNumber:", numbers[x])
#         print()
#     elif menu_choice == 2:
#         print("Add Name and Number")
#         name = input("Name: ")
#         phone = input("Number: ")
#         numbers[name] = phone
#     elif menu_choice == 3:
#         print("Remove Name and Number")
#         name = input("Name: ")
#         if name in numbers:
#             del numbers[name]
#         else:
#             print(name, "was not found")
#     elif menu_choice == 4:
#         print("Lookup Number")
#         name = input("Name: ")
#         if name in numbers:
#             print("The number is", numbers[name])
#         else:
#             print(name, "was not found")
#     elif menu_choice != 5:
#         print_menu()
#


# dict()
# value2 = 'value2'
# dct = {(0, 1): 'Large Dark Room'}
# player_loc = (0, 0)
#
# def move_right(loc):
#     return (loc[0], loc[1] + 1)
#
# print(dct[move_right(player_loc)])
#
# dct = {
#     'fruit': ['apple', ['banana', 'bananb'], 'grape'],
#     'people': {'names': ['Chris', 'Katie', 'Chelsea']}
#     }
#
# dct['fruit'][1] = 'GrapeFruit'
# print(dct['fruit'][1][0])
# print(len(dct['people']['names']))#['names'][0])
# print(dct['people']['names'])
# dct['people']['names'].append('Sheri')
# print(dct['people']['names'])
# dct['animals'] = ['Rex', 'TigerNice', 'phteven']
# print(dct)
# del dct['people']
# print(dct)

# phonebook = {
#     'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone': '5032779710'},
#     'dover': {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5551212122'},
# }
# def search(query):
#     old_fname = phonebook[query]['first_name'][:]
#     phonebook[query]['first_name'] = 'blah'
#     print(old_fname)
#     print()
#     print(phonebook[query]['first_name'])
#     # try:
#     #     print('Full Name: {} {}'.format(phonebook[query]['first_name'], phonebook[query]['last_name']))
#     #     print('Phone: {}'.format(phonebook[query]['phone']))
#     # except KeyError:
#     #     print('That is not a valid entry.')
#
# q = input("who are you looking for?: ").lower()
#
# search(q)

# LAB: PHONEBOOK
import csv



phonebook = {
    'jones': {'first': 'chris', 'last': 'jones', 'number': '32'},
    'harper': {'first': 'ryan', 'last': 'harper', 'number': '44'}
    }

is_running = True

def phone_print():
    print()
    for k in phonebook:
        print("{} {}: {}".format(
                                phonebook[k]['first'].capitalize(),
                                phonebook[k]['last'].capitalize(),
                                phonebook[k]['number'])
                                )
    print()

def phone_run():
    if input("Would you like to return to the menu? (y/n)").lower() == 'y':
        return True
    else:
        return False

def phone_search(query):
    try:
        print("{} {}: {}".format(
                                phonebook[query]['first'].capitalize(),
                                phonebook[query]['last'].capitalize(),
                                phonebook[query]['number'])
                                )
        return phonebook[query]
    except KeyError:
        return "User does not exist"

def phone_n_search(query):
    for k in phonebook:
        if query in phonebook[k]['number']:
            print("{} {}: {}".format(
                                    phonebook[k]['first'].capitalize(),
                                    phonebook[k]['last'].capitalize(),
                                    phonebook[k]['number'])
                                    )

def phone_add(first,last,number):
    temp_dict = {
                'first': first,
                'last': last,
                'number': number
                }
    phonebook[last] = temp_dict
    return temp_dict

def phone_del(last):
    try:
        print("Deleted {} {}'s contact".format(
                                        phonebook[last]['first'].capitalize(),
                                        phonebook[last]['last'])
                                        )
        del phonebook[last]
    except KeyError:
        return "User does not exist"

def phone_update(last):
    try:
        del phonebook[last]
        phone_add(
                    input("Type the first name: ").lower(),
                    input("Type the second name: ").lower(),
                    input("Type the number: ").lower()
                  )
    except KeyError:
        return "User could not be added"

while is_running:
    print("-----PHONE BOOK-----")
    phone_print()
    user = input("""Would you like to:\n
                    (C)reate a contact?\n
                    (R)etrieve a contact\n
                    (U)pdate a contact\n
                    (D)elete a contact\n
                    (F)ind contact from number\n
                    (Q)uit\n"""
                ).lower()

    if user == 'c':
        phone_add(
                    input("Type the first name: ").lower(),
                    input("Type the second name: ").lower(),
                    input("Type the number: ").lower()
                 )
        is_running = phone_run()
    elif user == 'r':
        phone_search(input("Please type the last name of the user: ").lower())
        is_running = phone_run()
    elif user == 'u':
        phone_update(input("Please type the last name of the user: ").lower())
        is_running = phone_run()
    elif user == 'd':
        phone_del(input("Please type the user's last name: "))
        is_running = phone_run()
    elif user == 'f':
        phone_n_search(input("Please type the user's phone number: "))
    elif user == 'q':
        print("QUITTING NOW...")
        is_running = False
