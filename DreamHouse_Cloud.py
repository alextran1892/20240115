import turtle
from turtle import Turtle
import random as r
def draw_cloud():
    cloud=turtle.Turtle()
    cloud.hideturtle()

    cloud_color_list = ['#C0C0BE','#CACAC8','#D4D4D2','#DEDEDC','#E8E8E6','#F2F2F0','#FCFCFA','#FFFFFF']
    cloud.pensize(2)

    cloud.penup()
    cloud.goto(-1000,500) #-1000, 500
    cloud.pendown()
    cloud.speed('fastest')
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