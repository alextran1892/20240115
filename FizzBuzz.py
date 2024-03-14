numb = input('Nhap hai so bat ky phan tach bang dau phay: ')
numb1 = numb.split(',')
a = int(numb1[0])
b = int(numb1[1])

#Xét điều kiện 1
if a>=b:
    for i in range(1,30):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%5 == 0:
            print('Buzz')
        elif i%3 == 0:
            print('Fizz')
        else:
            print(i)
else:
    print("Vui lòng nhập số a lớn hơn hoặc bằng số b")

