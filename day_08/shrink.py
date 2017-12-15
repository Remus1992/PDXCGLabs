# def convert_list (lo):
#     list_int = list(map(int, list(lo)))
#     return list_int
#
# def sum_values(sv):
#     summed = sum(sv)
#     return summed
#
# def convert_str (cs):
#     new_str = str(cs)
#     converted_list = list(map(int, list(new_str)))
#     return converted_list
#
# def sum_new_values(snw):
#     summed_new = sum(snw)
#     return summed_new
#
# list_original = input ("Enter a list of numbers separated by a comma and a space (ex: 5, 6, 7): ").replace(' ','').split(',')
#
# list_int = convert_list(list_original)
# print (list_int)
# summed = sum_values(list_int)
# print (summed)
# converted_list = convert_str(summed)
# print (converted_list)
# summed_new = sum_new_values(converted_list)
# print (summed_new)

# list_original = input ("Enter list: ").replace(' ','').split(',') #input string list
# list_int = list(map(int, list(list_original))) #convert to list of integers
# summed = sum(list_int) #calculate sum of list of integers
# my_string = str(summed) #convert to string
# print (my_string)
#
# while len(my_string) > 1: #while the length of the string is greater than one
#     my_string = list (my_string) #convert string to list of strings
#     for x in range(len(my_string)): #convert to string of integers
#         my_string[x] = int(my_string[x])
#
#     result = sum(my_string) #calculate sum of list of integers
#     print (result)
#     my_string = str (result) #reassign original string to result until length is no longer than 1


list_original = input ("Enter list: ").replace(' ','').split(',') #input string list
list_int = list(map(int, list(list_original))) #convert to list of integers
summed = sum(list_int) #calculate sum of list of integers
my_string = str(summed) #convert to string
print (my_string)

while len(my_string) > 1: #while the length of the string is greater than one
    my_string = list(map(int, list(my_string))) #convert to list of integers
    result = sum(my_string) #calculate sum of list of integers
    print (result)
    my_string = str (result) #reassign original string to result until length is no longer than 1
