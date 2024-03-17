import turtle as t
import random


#Tạo và quy định chiều dài rộng của đường đua và các tham số

screen = t.Screen()
screen.bgcolor('silver')
screen.setup(height=500, width=600)

#Hiển thị mà hình cho phép người dùng đoán con rùa màu nào thắng cuộc

guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")

#Danh sách lưu lại màu cho các con rùa tham chiến
colors = ['red', 'brown', 'blue', 'green', 'orange','pink']

#Cài đặt vị trí ban đầu cho các con rùa (x,y): x=-250
y_position = [0,-30,30,-60,60,90]

#Danh sách vận tốc của rùa để chọn ngầu nhiên
turtle_speed = [10,15,20,25,30,5]

#Danh sách lưu các con rùa
all_turtle = []
run = True

##Xây dựng hàm tạo các con rùa
for turtle in range (0,6):
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

##Chạy chương trình
while run:
    random_walk(all_turtle)
#Chương trình kết thúc khi click chuột lên màn hình
screen.exitonclick()
