import turtle

def draw_sail_boat():
    global sail_boat
    sail_boat = turtle.Turtle()
    sail_boat.speed('fastest')
    sail_boat.hideturtle()
    x = -1000
    y = 300
    for i in range(4):

        sail_boat.penup()
        sail_boat.goto(x,y)
        sail_boat.pendown()
        sail_boat.color('black')
        sail_boat.fillcolor('#235284')
        sail_boat.begin_fill()

        sail_boat.right(-10)
        sail_boat.forward(120)
        sail_boat.right(120)
        sail_boat.forward(10)
        sail_boat.right(60)
        sail_boat.forward(110)
        sail_boat.right(60)
        sail_boat.forward(10)
        sail_boat.end_fill()

        # sail_boat.penup()
        sail_boat.right(120)
        sail_boat.forward(65)
        # sail_boat.pendown
        sail_boat.pensize(3)
        sail_boat.right(-80)
        sail_boat.forward(100)

        sail_boat.pensize(1)
        sail_boat.fillcolor('light grey')
        sail_boat.begin_fill()
        sail_boat.right(160)
        sail_boat.forward(70)
        sail_boat.right(60)
        sail_boat.forward(35)
        sail_boat.end_fill()

        sail_boat.penup()
        sail_boat.home()
        sail_boat.pendown()
        x+=500


# draw_sail_boat()
# turtle.done()

