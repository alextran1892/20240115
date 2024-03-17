# In put list of int need to be sorted, seperate by coma ,

input_int = input('Entry list of int need to be sorted, seperate by coma: ')

a = input_int.split(',')
origin_list = []
for i in a:
    origin_list.append(int(i))

def find_min_inList(origin_list):
    min = origin_list[0]
    for i in origin_list:
        if i < min:
            min = i
    print(min)
find_min_inList(origin_list)