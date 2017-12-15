# reqirements:
# name
# account number
# account balance
# phone number

# accounts = {
#         000001: {
#         'name': 'Chris',
#         'phone': 5032779710,
#         'balance': 10.00
#         }
#     }

NUMBER_OF_ACCOUNTS = 0

class BankAccount:
    def __init__(self, client_name, phone):
        self.account_number = self.assign_account_number()
        self.name = client_name
        self.phone = phone
        self.balance = 0

    def assign_account_number(self):
        global NUMBER_OF_ACCOUNTS
        NUMBER_OF_ACCOUNTS += 1
        # return BankAccount.objects.all().count() + 1
        return NUMBER_OF_ACCOUNTS

    def deposit(self, amount):
        self.balance += amount
        print("Thanks {}! Your balance is now ${}.".format(self.name, self.balance))


    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("Thanks {}! Your balance is now ${}.".format(self.name, self.balance))
        else:
            print("I'm sorry {}, you do not have enough money for that.".format(self.name))



class BankAccountPlus(BankAccount):
    def __init__(self, name, phone):
        super().__init__(name, phone)

    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            print("Thanks {}! Your balance is now ${}.".format(self.name, self.balance))
        elif 100 > self.balance - amount > 0:
            print("I'm sorry {}, that would put you below $100.".format(self.name))
        else:
            print("I'm sorry {}, you do not have enough money for that.".format(self.name))



if __name__ == "__main__":
    sheri_account = BankAccount('Sheri', 5416025555)
    chris_account = BankAccountPlus('Chris', 5032779710)
    # accounts = []
    # accounts.append(BankAccount('Sheri', 5416025555))
    # accounts.append(BankAccount('Chris', 5032779710))
    # while True:
    #     query = input("What would you like to do. ")
    #     if query == '1':
    #

    print(sheri_account.name)
    sheri_account.deposit(1000)
    sheri_account.withdraw(900)

    print()

    print(chris_account.name)
    chris_account.deposit(100)
    chris_account.withdraw(90)
