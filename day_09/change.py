# change = float(0.76)
# change *= 100
#
# quarter = 25
# dime = 10
# nickel = 5
# penny = 1



def change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in change(n, coins_available[1:], coins_so_far):
            yield c

n = 24
coins = [1, 5, 10, 25]

solutions = [s for s in change(n, coins, [])]
for s in solutions:
    print (s)
#
# print ('Optimal Solutions: ', min(solutions, key = len))


# target = 200
# coins = [1,2,5,10,20,50,100,200]
# ways = [1]+[0]*target
# for coin in coins:
#     for i in range(coin,target+1):
#         ways[i]+=ways[i-coin]
# print(ways[target])

# # USD - $1, $5, $10, etc.
# currency = [1, 5, 10, 20, 50, 100]
#
#
# def minimum_bills_to_make_change(amount):
#
#     # initialize arrays for $0
#     minimum_number_of_currency = [10000]*(amount+1)
#     minimum_number_of_currency[0] = 0
#
#     for i in xrange(1, amount + 1):
#         for j in currency:
#             if i - j > -1:
#                 minimum_number_of_currency[i] =\
#                     min(minimum_number_of_currency[i], minimum_number_of_currency[i - j] + 1)
#
#     return minimum_number_of_currency[amount]
#
#
# minimum_bills_to_make_change (120)


# # USD - $1, $5, $10, etc.
# currency = [1, 5, 10, 20, 50, 100]
#
# # the amount to change - $120
# amount = 120
#
# # initialize arrays for $0
# minimum_number_of_currency = [0]
# currency_composition = [[]]
#
# for i in xrange(1, amount + 1):
#     best = 10000
#     best_currency_composition = None
#
#     for j in currency:
#         if i - j > -1 and minimum_number_of_currency[i - j] + 1 < best:
#             best = minimum_number_of_currency[i - j] + 1
#             best_currency_composition = currency_composition[i - j] + [j]
#
#     minimum_number_of_currency.append(best)
#     currency_composition.append(best_currency_composition)
#
#     print '{0:3} {1} {2}'.format(i, best, best_currency_composition)
