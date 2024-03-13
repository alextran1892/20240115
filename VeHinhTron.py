import turtle
import math

r = int(input('Entry the radius: '))
t = turtle.Turtle()
Screen = turtle.Screen()
Screen.bgcolor('silver')

c = round(2 * math.pi * r,2)
s = round(math.pi * r * r,2)

#kích thước viền hình tròn
t.pensize(10)
#màu sắc viền hình tròn
t.pencolor('#808080')
#tùy chỉnh điểm bắt đầu vẽ hình tròn
t.penup()
t.goto(-200,-200)
t.pendown()

#màu nền hình tròn
t.fillcolor('#ff69b4')
t.begin_fill()
#bán kính hình tròn r
t.circle(r)
t.end_fill()

t.hideturtle()

#Hiển thị chu vi và diện tích bên cạnh hình tròn
Chat=turtle.Turtle()
Chat.pensize(5)
Chat.pencolor('pink')
Chat.speed(5)
Chat.penup()
Chat.goto(100,100) 
Chat.pendown()
Chat.left(60)
Chat.forward(40)
Chat.right(60)


for loop in range(10):
    Chat.circle(25,90)
    Chat.right(120)

Chat.goto(100,100)
Chat.penup()
Chat.right(70)
Chat.forward(80)
Chat.pendown()
Chat.write('''C = : {c}
S = : {s} '''.format(c=c,s=s), align="center", font=("Arial", 13, "normal"))

Chat.hideturtle()
turtle.mainloop()

