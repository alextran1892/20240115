import turtle
def draw_umbrella():
    umbrella = turtle.Turtle()
    umbrella.hideturtle()
    umbrella.speed('fastest')
    umbrella_size = 35

    a = -800
    b = -250
    for k in range(4):
        umbrella.left(-20)
        umbrella.penup()
        umbrella.goto(a,b)
        umbrella.pendown()
        #Umbrella stand
        for loop in range(2):
            umbrella.fillcolor('grey')
            umbrella.begin_fill()
            umbrella.circle(umbrella_size,90)
            umbrella.circle(umbrella_size/2,90)
            umbrella.end_fill()
        #Umbrella stick
        umbrella.right(-65)
        umbrella.forward(30)
        umbrella.left(45)
        umbrella.pensize(5)
        umbrella.forward(250)
        x = umbrella.position()
        #Umbrella 
        umbrella.pensize(1)
        umbrella.fillcolor('#ff9f00')
        umbrella.begin_fill()
        umbrella.left(175)
        umbrella.forward(200)
        for i in range (10):
            umbrella.left(120)
            umbrella.forward(40)
            y = umbrella.position()
            umbrella.goto(x)
            umbrella.goto(y)
            umbrella.left(10)
            umbrella.end_fill()
        a+=500
        umbrella.penup()
        umbrella.home()
        umbrella.pendown()

# draw_umbrella()
# turtle.done()