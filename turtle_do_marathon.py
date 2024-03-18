import turtle as t
import random
import time



#Tạo khung cảnh và vẽ các cột mốc
#Tạo và quy định chiều dài rộng của đường đua và các tham số

screen = t.Screen()
screen.bgcolor('silver')
screen.setup(height=500, width=600)

pen =  t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250,200)
for i in range(21):
    pen.write(i)
    pen.forward(25)

#Vẽ các đường đứt đoạn trên đường đua + đánh dấu các cột mốc bên phải đường đua
x = -250
pen.goto(-250,200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x + (i+1)*25,200)


#Hiển thị mà hình cho phép người dùng đoán con rùa màu nào thắng cuộc

guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")

#Danh sách lưu lại màu cho các con rùa tham chiến
colors = ['blue', 'green', 'orange','pink']

#Cài đặt vị trí ban đầu cho các con rùa (x,y): x=-250
y_position = [160, 100, 40, -20]

#Danh sách vận tốc của rùa để chọn ngầu nhiên
turtle_speed = [5,10,15,20]

#Danh sách lưu các con rùa
all_turtle = []
run = True

##Xây dựng hàm tạo các con rùa
for turtle in range (0,4):
    turtles = t.Turtle(shape='turtle')
    turtles.penup()
    #Di chuyển rùa về vị trí xuất phát
    turtles.goto(x=-250, y=y_position[turtle])
    #Màu của rùa
    turtles.color(colors[turtle])
    #Lưu vào danh sách
    all_turtle.append(turtles)

##Xây dựng hàm di chuyển cho các con rùa
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        #Kiểm tra điều kiện cán đích. Khi 1 con rùa bất kỳ cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False
            #Xác định thời gian kết thúc cuộc đua
            end_time = time.time()
            #Tính thời gian chạy của các con rùa
            elapsed_time = end_time - start_time

            #Thông báo con rùa chiến thắng
            notice1 = t.Turtle()
            notice1.penup()
            notice1.goto(-300,-200)
            notice1.pendown()
            notice1.write('Con rùa chiến thắng là', font=("Arial", 16, "normal"))
            turtle.goto(-300,-250)
            
            #Hiển thị thời gian chay đua của rùa
            notice2 = t.Turtle()
            notice2.penup()
            notice2.goto(-300,-300)
            notice2.pendown()
            a = print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
            notice2.write('Thời gian chạy của rùa' +' ' + str(round(elapsed_time,2)) + 'sec', font=("Arial", 16, "normal"))


##Chạy chương trình
while run:
    random_walk(all_turtle)
     #Xác định thời gian rùa bắt đầu chạy
    start_time = time.time()
    
#Chương trình kết thúc khi click chuột lên màn hình
screen.exitonclick()
