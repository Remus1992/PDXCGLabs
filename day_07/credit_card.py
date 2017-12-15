#Validate credit card number "4556737586899855"

def slice_last(s):
    list_card_int = list(map(int, list(s)))
    final_value = list_card_int[-1]
    truncated_list = list_card_int.pop()
    return list_card_int, final_value

def reverse_digits(r):
    reversed_list = list(reversed(r))
    return reversed_list

def double_others(d):
    for x in range(len(d)):
        if x % 2 == 0:
            d[x] *= 2
    doubled = d
    return doubled

def subtract_nine(sb):
    for x in range(len(sb)):
        if sb[x] > 9:
            sb[x] -= 9
    subtracted_num = sb
    return subtracted_num

def sum_values(sv):
    summed = sum(sv)
    return summed

def second_digit(sd):
    str_sd = str(sd)
    str_sd.strip()
    second_num_str = str_sd[-1]
    second_num = int(second_num_str)
    return second_num

def validate(v1, v2):
    val_1 = v1
    val_2 = v2
    if val_1 == val_2:
        print ("Valid Credit Card Number")
    else:
        print ("Invalid Credit Card Number")



card_number = "4556737586899855"
# print (list(map(int, list(s))))
list_card_int, final_value = slice_last(card_number)
# print (list_card_int)
# print (final_value)
reversed_list = reverse_digits (list_card_int)
# print (reversed_list)
doubled = double_others (reversed_list)
# print (doubled)
subtracted_num = subtract_nine(doubled)
# print (subtracted_num)
summed = sum_values(subtracted_num)
# print (summed)
second_num = second_digit(summed)
# print (second_num)
# print (final_value)
validate(final_value, second_num)
