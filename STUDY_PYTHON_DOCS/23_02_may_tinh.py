import tao_may_tinh

a = int(input('Nhap vao a: '))
b = int(input('Nhap vao b: '))
Phep_tinh = input('Nhap vao phep tinh + hoac - hoac * hoac /: ')
if Phep_tinh == '+':
    print(a,Phep_tinh,b,'=',tao_may_tinh.cong(a,b))
        
elif Phep_tinh == '-':
    print(a,Phep_tinh,b,'=',tao_may_tinh.tru(a,b))
       
elif Phep_tinh == '*':
   print(a,Phep_tinh,b,'=',tao_may_tinh.nhan(a,b))
        
elif Phep_tinh == '/':
    print(a,Phep_tinh,b,'=',tao_may_tinh.chia(a,b))
        
else:
    print('Vui long nhap lai phep tinh theo huong dan')

