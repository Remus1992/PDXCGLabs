# my_string = "345"
#
# while len(my_string) > 1:
#     my_string = list (my_string)
#     for x in range(len(my_string)):
#         my_string[x] = int(my_string[x])
#
#     result = sum(my_string)
#     print (result)
#     my_string = str(result)



list_original = input ("Enter list: ").replace(' ','').split(',')
# print (list_original)
list_int = list(map(int, list(list_original)))
summed = sum(list_int)
# print (summed)
my_string = str(summed)
print (my_string)

# my_string = "18"

while len(my_string) > 1:
    my_string = list (my_string)
    for x in range(len(my_string)):
        my_string[x] = int(my_string[x])

    result = sum(my_string)
    print (result)
    my_string = str (result)

    #
    # list_int = list(map(int, list(lo)))
    # summed = sum(list_int)
    # new_str = str(summed)
    # if len(new_str) > 0
    #     converted_list = list(map(int, list(new_str)))
    #     shrunk = sum(converted_list)
    #     return shrunk
    # else break
