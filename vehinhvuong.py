import turtle
t = turtle.Turtle()
t.pensize('10')
t.pencolor('gray')
t.fillcolor("pink")
t.begin_fill()

for i in range (4):
    t.forward(100)
    t.right(90)  

t.end_fill()
t.done()