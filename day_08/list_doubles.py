def convert_list (lo):
    list_int = list(map(int, list(lo)))
    return list_int

def double_list (dl):
    list_before = dl
    doubled = [x * 2 for x in list_before]
    return doubled

list_original = input ("Enter a list of numbers separated by a comma and a space (ex: 5, 6, 7): ").replace(' ','').split(',')

list_int = convert_list(list_original)
print (list_int)
doubled = double_list(list_int)
print (doubled)
