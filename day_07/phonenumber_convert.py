# print 5032779710 -> "(503)277-9710"

##Option 1
def pretty_print(num):
    first_third = num[0:3]
    second_third = num[3:6]
    third_third = num[6:10]
    print ('Formated Number is: ({}){}-{}'.format(first_third, second_third, third_third))
    return

phone_number = input("Nine Digit Phone Number: ")
pretty_print (phone_number)


##Option 2
# pretty_number = {}
#
# def pretty_print(num):
#     first_third = num[0:3]
#     second_third = num[3:6]
#     third_third = num[6:10]
#     pretty_number[num] = {'first_third': first_third, 'second_third': second_third, 'third_third': third_third}
#     return
#
# phone_number = input("Nine Digit Phone Number: ")
# pretty_print (phone_number)
#
# print('Formated Number is: ({}){}-{}'.format(pretty_number[phone_number]['first_third'], pretty_number[phone_number]['second_third'], pretty_number[phone_number]['third_third']))


##Option 3
# def first_third(num):
#     return num[0:3]
#
# def second_third(num):
#     return num[3:6]
#
# def third_third(num):
#     return num[6:]

# phone_number = input("Nine Digit Phone Number: ")
#
# first_third = first_third(phone_number)
# second_third = second_third(phone_number)
# third_third = third_third(phone_number)
#
# print ("({}){}-{}".format(first_third, second_third, third_third))
