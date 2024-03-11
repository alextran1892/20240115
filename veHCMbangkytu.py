char = input('Nhap ky tu: ')
Chieu_dai = int(input('Nhap Chieu dai: '))
Chieu_rong = int(input('Nhap Chieu rong: '))

for i in range(1,Chieu_rong + 1):
    print_str = ''
    for j in range(1,Chieu_dai + 1):
        if i == 1 or i == Chieu_rong:
            print_str += char
        else:
            if j == 1 or j == Chieu_dai:
                print_str += char
            else:
                print_str += ' '
    print(print_str)