import turtle
#define pen size
turtle.pensize(5)

#define pen color
turtle.pencolor('pink')

#for outline bigger circle
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)

#for eyes
#eyes color is black
turtle.fillcolor('black')
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()

#khai bao bien eye size kich thuoc mat
eye_size = 20

turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()

turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#for nose
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.circle(-70, steps=3)

#for smile
turtle.penup()
turtle.goto(-100,-70)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()
