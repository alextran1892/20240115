
import turtle
from random import randint
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor('light pink')

spiral = turtle.Turtle()
spiral.shape('turtle')


d = 1

while True:
    spiral.color(randint(0,255),randint(0, 255),randint(0, 255))
    spiral.pensize(10)
    spiral.speed(0.5)
    spiral.right(20)
    spiral.forward(d)
    #Xác định tọa độ mới của rùa sau khi di chuyển
    x = spiral.xcor() #Gán x là hoành độ
    y = spiral.ycor() #Gán y là tung độ
    distance = float((x**2 + y**2)*0.5) #Tính khoảng cách từ điểm hiện tại đến tâm (0,0)
    d +=1
    if distance > 60000:
        break

spiral.penup()
spiral.goto(0,0)
spiral.pendown()
spiral.pensize(10)
spiral.pencolor('brown')
spiral.goto(0, -500)
spiral.hideturtle()

#for the chat
Chat=turtle.Turtle()
Chat.pensize(5)
Chat.pencolor('red')
Chat.speed(0.5)
Chat.penup()
Chat.goto(250,250) 
Chat.pendown()
Chat.left(60)
Chat.forward(40)
Chat.right(60)


for loop in range(10):
    Chat.circle(25,90)
    Chat.right(120)

Chat.goto(250,250)
Chat.penup()
Chat.right(70)
Chat.forward(80)
Chat.pendown()
Chat.write("""Wish you all the best
 tomorrow ❤!""", align="center", font=("Arial", 9 , "bold"))

Chat.hideturtle()

turtle.hideturtle()

turtle.done()