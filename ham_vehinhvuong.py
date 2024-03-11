import turtle
t = turtle.Turtle()
t.pencolor('black')
t.pensize(15)
turtle.bgcolor('red')
t.fillcolor('yellow')
t.begin_fill()
t.goto(-100,100)
def ve_HV(v):
    for i in range(4):
        t.forward(v)
        t.right(90)
    t.end_fill()
    turtle.done()
   
ve_HV(250)