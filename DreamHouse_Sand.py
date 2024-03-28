import turtle
from turtle import Turtle
import random as r
def draw_sand():
    sand = turtle.Turtle()
    sand.shape('turtle')
    sand.hideturtle()
    sand.color('#dbd5b4')
    sand.pensize(2)
    sand.penup()
    sand.goto(-1000,0)
    sand.pendown()
    sand.showturtle()

    for i in range (2):
            sand.pencolor('#dbd5b4')
            sand.fillcolor('#dbd5b4')
            sand.begin_fill()
            sand.forward(2000)
            sand.right(90)
            sand.forward(133)
            sand.right(90)
            sand.end_fill()
    y = 0
    for k in range(25):
        sand.hideturtle()
        sand.penup()
        sand.goto(-950,y)
        sand.pendown()
        for i in range(100):
            sand.showturtle()
            sand.speed('fastest')
            #Set màu cho hột cát
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

# draw_sand()
# turtle.done()