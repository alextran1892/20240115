sotiendachi = float(input('Nhap vao so tien da chi:'))
sotiendonhanghientai = float(input('Nhap vao so tien don hang hien tai:'))

if sotiendachi >= 150:
    print('sotienthanhtoan =: ', sotiendonhanghientai-50)
elif sotiendachi >= 100:
     print('sotienthanhtoan =: ', sotiendonhanghientai-25)
elif sotiendachi >= 75:
      print('sotienthanhtoan =: ', sotiendonhanghientai-15)
else:
      print('sotienthanhtoan =: ', sotiendonhanghientai)