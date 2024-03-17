import turtle
import random as r

#Tạo danh sách màu cho biển và sóng
wave_color_list = ['#235284', '#3271a5','#3982b8', '#4194cb', '#46a2da','#58afdd', '#6abce2', '#8dcfec', '#b8e2f4']

pen = turtle.Turtle()
pen.shape('turtle')
pen.color('gray')
#Phân cách trời và biển
# pen.penup()
# pen.goto(0,333)
# pen.pendown()
# pen.forward(1000)
# pen.backward(2000)

#Tô màu trời
pen.penup()
pen.goto(-1000,333)
pen.pendown()
pen.speed(100)

for i in range (2):
    pen.pencolor('#8dcfec')
    pen.fillcolor('#8dcfec')
    pen.begin_fill()
    pen.forward(2000)
    pen.left(90)
    pen.forward(500)
    pen.left(90)
    pen.end_fill()
#Mây
cloud=turtle.Turtle()
cloud.hideturtle()
# cloud_color_list = ['#DAE1E9','#AEBECD','#90A5BA',]
cloud_color_list = ['#C0C0BE','#CACAC8','#D4D4D2','#DEDEDC','#E8E8E6','#F2F2F0','#FCFCFA','#FFFFFF']
cloud.pensize(2)

cloud.penup()
cloud.goto(-1000,500) #-1000, 500
cloud.pendown()
cloud.showturtle()
cloud.speed(100)
ban_kinh1 = [50,60,70,80,90,100,120,130,140,150,180]
x = 50
for loop in range(100):
    a = cloud_color_list[r.randint(0,len(cloud_color_list)-1)]
    cloud.pencolor(a)
    cloud.fillcolor(a)
    cloud.begin_fill()
    cloud.right(45)
    cloud.circle(ban_kinh1[r.randint(0,len(ban_kinh1)-1)],90)
    cloud.goto(-1000,500)
    cloud.end_fill()
    cloud.right(45)
    cloud.forward(x)
    x+=20
#Tô màu biển
pen.penup()
pen.goto(-1000,333)
pen.pendown()
pen.speed(100)
for k in range(9):
    for i in range (2):
        pen.pencolor(wave_color_list[k])
        pen.fillcolor(wave_color_list[k])
        pen.begin_fill()
        pen.forward(2000)
        pen.right(90)
        pen.forward(37)
        pen.right(90)
        pen.end_fill()
    pen.right(90)
    pen.forward(37)
    pen.left(90)

#Test sóng
all_waves = []
run = True

y_position = [290,275,260,245,230,215,200,185,170,155,140,125,110,95,80,65,50,35,20,5,]
for wave in range(0,20):
    waves = turtle.Turtle(shape='turtle')
    waves.penup()
    waves.goto(x=-1000, y=y_position[wave])
    waves.speed(100)
    waves.pensize(5)
    waves.color(wave_color_list[r.randint(0,len(wave_color_list)-1)])
    all_waves.append(waves)

def draw_wave(waves):
    for i in range(50):
        global run
        for wave in waves:
            #Cài đặt màu ngẫu nhiên cho mỗi bước 
            wave.pencolor(wave_color_list[r.randint(0,len(wave_color_list)-1)])
            down = r.randint(10,40)
            up = r.randint(10,40)
            wave.pendown()
            #Rùa tiến lên phía trước với giá trị ngẫu nhiên có để lại nét vẽ
            wave.circle(down/2,90)
            wave.circle(-down/2,-90)
            wave.right(180)
            wave.penup()
            #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
            wave.forward(up)
        if wave.xcor() > 1000:
            run = False
while run:
    draw_wave(all_waves)

# #Sóng biển
# wave = turtle.Turtle()
# wave.shape('turtle')
# wave.hideturtle()
# wave.pensize(5)
# wave.speed(10000000)
# wave.penup()

# y = 290
# for k in range(20):

#     wave.goto(-1000,y)
#     wave.penup()
#     #Hiển thị hình ảnh rùa
#     wave.showturtle()


# #T.color(danh_sach_mau[T.random.randint(0, len(danh_sach_mau) - 1)])
#     for i in range(50):

#         #Set màu ngẫu nhiên cho sóng
#         wave.pencolor(wave_color_list[r.randint(0,len(wave_color_list)-1)])
#         #sinh hai giá trị ngầu nhiên
#         down = r.randint(10,40)
#         up = r.randint(10,40)
#         wave.pendown()
#         #Rùa tiến lên phía trước với giá trị ngẫu nhiên có để lại nét vẽ

#         wave.circle(down/2,90)
#         wave.circle(-down/2,-90)
#         wave.right(180)
#         wave.penup()
#         #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
#         wave.forward(up)
#     y-=15   

#mặt trời
sun_color_list = ['#FFF3E0','#FFE0B2','#FFCC80','#FFB74D','#FFA726','#FF9800','#FB8000','#F57000','#EF6C00','#E65100']

sun = turtle.Turtle()
sun.speed(100)
sun.pensize(1)
sun.penup()
sun.goto(400,333)
sun.right(90)
sun.pendown()
r = 300
x = 350
for i in range (10):
    sun.pencolor(sun_color_list[i])
    sun.fillcolor(sun_color_list[i])
    sun.begin_fill()
    sun.circle(r,-180)
    sun.penup()
    sun.goto(x,333)
    sun.right(180)
    sun.pendown()
    r-=30
    x+=30
    sun.end_fill()

# Đàn chim trời
bird = turtle.Turtle()
bird.pensize(3)
bird.color('black')
bird.speed(1000)
bird.penup()
bird.goto(450,450)
b = 122
for i in range(6):
    a= bird.pos()
    bird.pendown()
    bird.forward(15)
    bird.backward(15)
    bird.left(10)
    bird.circle(15,80)
    bird.penup()
    bird.goto(a)
    bird.pendown()
    bird.left(10)
    bird.circle(15,80)
    bird.penup()
    bird.goto(a)
    bird.left(b)
    bird.forward(45)
    bird.pendown()
    b+=15
bird.hideturtle()
import random as r
#Cát
sand = turtle.Turtle()
sand.shape('turtle')
sand.hideturtle()
sand.color('#F1BB5E')
sand.pensize(2)
sand.penup()
sand.goto(-1000,0)
sand.pendown()
sand.showturtle()

for i in range (2):
        sand.pencolor('#F1BB5E')
        sand.fillcolor('#F1BB5E')
        sand.begin_fill()
        sand.forward(2000)
        sand.right(90)
        sand.forward(133)
        sand.right(90)
        sand.end_fill()
y = 0
for k in range(10):
    sand.hideturtle()
    sand.penup()
    sand.goto(-950,y)
    sand.pendown()
    for i in range(100):
        sand.showturtle()
        sand.speed(10000)
        #Set màu ngẫu nhiên cho sóng
        sand.pencolor('brown')
        #sinh hai giá trị ngầu nhiên
        up = r.randint(5,35)
        sand.pendown()
        #Rùa tiến lên phía trước với giá trị ngẫu nhiên có để lại nét vẽ
        sand.forward(1)
        sand.penup()
        #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
        sand.forward(up)
    y-=5

# Kết thúc vẽ
#Mountain

#House

#Fence

#House Body

#Porch

#Stairs

#Roof

#Windows

#Door

turtle.mainloop()

