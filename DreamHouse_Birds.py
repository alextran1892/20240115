import turtle
def draw_birds():
    bird = turtle.Turtle()
    bird.hideturtle()
    bird.pensize(3)
    bird.color('black')
    bird.speed('fastest')
    bird.penup()
    bird.goto(450,450)
    b = 122
    for i in range(6):
        a= bird.pos()
        bird.pendown()
        bird.forward(15)
        bird.backward(15)
        bird.left(10)
        bird.circle(15,80)
        bird.penup()
        bird.goto(a)
        bird.pendown()
        bird.left(10)
        bird.circle(15,80)
        bird.penup()
        bird.goto(a)
        bird.left(b)
        bird.forward(45)
        bird.pendown()
        b+=15