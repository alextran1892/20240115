import turtle
from turtle import Screen, Turtle
import random as r
turtle_color_list = ['#235284', '#3271a5','#3982b8', '#4194cb', '#46a2da','#58afdd', '#6abce2', '#8dcfec', '#b8e2f4']
#Turtle
def draw_turtle_on_the_sea():
    all_turtles = []
    global run
    run = True
    x_position = [-600, -400, -200, 0, 50, 10]
    y_position = [290,155,95,65,35,20,5]
    for turtle in range(0,5):
        turtles = Turtle(shape="turtle")
        turtles.penup()
        turtles.goto(x=x_position[r.randint(0,len(x_position)-1)], y=y_position[r.randint(0,len(y_position)-1)])
        turtles.speed(100)
        turtles.pensize(1)
        turtles.color(turtle_color_list[r.randint(0,len(turtle_color_list)-1)])
        all_turtles.append(turtles)

    def draw_turtle(turtles):
        global run
        for turtle in turtles:
            #Cài đặt màu ngẫu nhiên cho mỗi bước 
            turtle.pencolor(turtle_color_list[r.randint(0,len(turtle_color_list)-1)])
            down = r.randint(10,40)
            up = r.randint(10,40)
            turtle.pendown()
            turtle.penup()
            #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
            turtle.forward(up)
            if turtle.xcor() > 600:
                turtle.right(180)
                turtle.forward(down)
            elif turtle.xcor() < -600:
                turtle.right(180)
                turtle.forward(down)
    while run:
        draw_turtle(all_turtles)
draw_turtle_on_the_sea()