Age = int(input('Enter your age: '))
if Age > 20:
    print("""Okie, Let's go to next step""")
    weight = float(input('Enter your weight in Kg: '))
    height = float(input('Enter your height in m: '))
    BMI = weight/height**2

    if BMI > 40: 
        print('Béo phì cấp độ III')
    elif  35 <= BMI < 40: 
        print('Béo phì cấp độ II')
    elif  30 <= BMI < 35:
        print('Béo phì cấp độ I')
    elif  25 <= BMI < 30: 
        print('Thừa cân')
    elif  18.5 <= BMI < 25:
        print('Bình thường')
    elif  17 <= BMI < 18.5:
        print("Gầy cấp độ I")
    elif  16 <= BMI < 17: 
        print("Gầy cấp độ II")
    elif BMI < 16:
        print("Gầy cấp độ III")
else:
    print('Sorry BMI is not applied for the Age under 20')


