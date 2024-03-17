

# In put list of int need to be sorted, seperate by coma ,

input_int = input('Entry list of int need to be sorted, seperate by coma: ')

a = input_int.split(',')
origin_list = []
for i in a:
    origin_list.append(int(i))

print(origin_list)


def sort_input_int(origin_list):
    sorted_list = sorted(origin_list)
    print('sorted_input_int: ', sorted_list)

sort_input_int(origin_list)

