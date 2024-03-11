day_so_co_san = [6,8,2,9,1,7]
max = day_so_co_san[0]
max2 = 0
for i in day_so_co_san:
    if i > max:
        max = i
for k in day_so_co_san:
    if k > max2 and k < max:
        max2 = k
print(max2)

min = day_so_co_san[0]
for j in day_so_co_san:
    if j < min:
        min = j
print(min)

day_so_co_san.sort(reverse=True)
print(day_so_co_san[1])