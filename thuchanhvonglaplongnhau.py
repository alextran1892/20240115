import turtle
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('star')

myPen = turtle.Turtle()
myPen.speed(15)
myPen.color('pink')

for j in range (1,100):
    for i in range (1,6):
        myPen.left(144)
        myPen.forward(200)
    myPen.left(5)
turtle.done()