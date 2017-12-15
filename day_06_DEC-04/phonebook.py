phonebook = {
    # 'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone_number': '5412813629'},
}


def new_entry():
    new_first_name = input("Enter New First Name: ").title()
    new_last_name = input("Enter New Last Name: ").title()
    new_phone_number = int(input("Enter New Phone Number: "))
    # {'new_key': {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_phone_number': new_phone_number}}
    phonebook[new_last_name] = {'first_name': new_first_name, 'last_name': new_last_name, 'phone_number': new_phone_number}
    return

def search_entry(query):
    try:
        print('Full Name: {} {}'.format(phonebook[query]['first_name'], phonebook[query]['last_name']))
        print('Phone: {}'.format(phonebook[query]['phone_number']))
    except KeyError:
         print("That is Not a Valid Entry.")

def edit_entry(ammendment):
    del phonebook[ammendment]
    new_first_name = input("Enter New First Name: ").title()
    new_last_name = input("Enter New Last Name: ").title()
    new_phone_number = int(input("Enter New Phone Number: "))
    # {'new_key': {'new_first_name': new_first_name, 'new_last_name': new_last_name, 'new_phone_number': new_phone_number}}
    phonebook[new_last_name] = {'first_name': new_first_name, 'last_name': new_last_name, 'phone_number': new_phone_number}
    return

def delete_contact (excise):
    del phonebook[excise]
    return

def print_directory ():
    for i in phonebook:
            print('Full Name: {} {} - Phone Number: {}'.format(phonebook[i]['first_name'], phonebook[i]['last_name'], phonebook[i]['phone_number']))

def command_line_prompt():
    while True:
        print('1. Add a Contact (new)')
        print('2. Lookup a Contact (search)')
        print('3. Edit a Contact (edit)')
        print('4. Remove a Contact (delete)')
        print('5. Print Directory (directory)')
        print('6. Quit (quit)')
        # print('Do you wish to add a new contact (new), search for a contact (search), edit an existing contact (edit), or delete a contact (delete)?: ')
        option = input().lower()
        # if option in 'new search edit delete'.split()
        if option == 'new' or option == '1':
            new_entry()
        elif option == 'search' or option == '2':
            q = input("What is the last name of the person you are looking for?: ").title()
            search_entry(q)
        elif option == 'edit' or option == '3':
            a = input("what is the last name of the person you are wanting to edit?: ").title()
            edit_entry(a)
        elif option == 'delete' or option == '4':
            x = input("what is the last name of the person you are wanting to delete?: ").title()
            delete_contact(x)
        elif option == 'directory' or option == '5':
            print_directory()
        elif option == 'quit' or option == '6':
            break
        else:
            print('Please enter your option exclusively as either "new" or "search" or "edit" or "delete".')

command_line_prompt()
