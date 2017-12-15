# def hello_func(greeting, gremlin = 'gremlin'):
#     return '{} {}'.format(greeting, gremlin)
#
# print(hello_func('Hi'))
# print(hello_func('Remington', 'Henderson'))
# print(hello_func('Henderson', gremlin = 'Remington'))



month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month():
    print('Enter Month: ')
    return int(input())

def get_year():
    print('Enter Year: ')
    return int(input())

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

year = get_year()
month = get_month()

print (days_in_month(year, month))
