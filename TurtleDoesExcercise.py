import turtle
import random as r
#Set màu nền cho biển
Screen = turtle.Screen()
Screen.bgcolor('#6abce2')
wave_color_list = ['#235284', '#3271a5','#3982b8', '#4194cb', '#46a2da','#58afdd', '#6abce2', '#8dcfec', '#b8e2f4']

wave = turtle.Turtle()
wave.shape('turtle')
wave.hideturtle()
wave.pensize(5)
wave.speed(0.5)
wave.penup()

#đặt rùa ở vị trí bên trái màn hình 400 pixels

y = 0
for k in range(10):

    wave.goto(-1000,y)
    wave.penup()
    #Hiển thị hình ảnh rùa
    wave.showturtle()


#T.color(danh_sach_mau[T.random.randint(0, len(danh_sach_mau) - 1)])
    for i in range(50):

        #Set màu ngẫu nhiên cho sóng
        wave.pencolor(wave_color_list[r.randint(0,len(wave_color_list)-1)])
        #sinh hai giá trị ngầu nhiên
        down = r.randint(20,50)
        up = r.randint(20,50)
        wave.pendown()
        #Rùa tiến lên phía trước với giá trị ngẫu nhiên có để lại nét vẽ

        wave.circle(down/2,90)
        wave.circle(-down/2,-90)
        wave.right(180)
        wave.penup()
        #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
        wave.forward(up)
    y+=10

turtle.done()
