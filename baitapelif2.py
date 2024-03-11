a = float(input('nhap a:'))
b = float(input('nhap b:'))
c = float(input('nhap c:'))
if a>b:
    if a>c:
        print( 'a la so lon nhat')
    elif a == c :
        print('a va c là so lon nhat')
    else :
        print('c la so lon nhat')
elif a == b :
    print('a va b là so lon nhat')
else :
    print('b la so lon nhat')
