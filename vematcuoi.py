import turtle
#define screen
Screen=turtle.Screen()
Screen.bgcolor('gray')



#for outline bigger circle
face=turtle.Turtle()
face.pensize(5)
face.pencolor('brown')
facesize = 200
face.fillcolor('#ffe4e1')
face.penup()
face.goto(0, -200)
face.pendown()
face.begin_fill()
face.circle(facesize)
face.end_fill()
face.hideturtle()


#for eyes

eye=turtle.Turtle()
eye.fillcolor('#f5f5f5')
eye.pensize(2)
eye.pencolor('black')
eye.penup()
eye.goto(-100,50)
eye.right(45)
eye.pendown()
eye.hideturtle()

#khai bao bien eye size kich thuoc mat
eye_size = 20

eye.begin_fill()

for loop in range(2):
    eye.circle(eye_size,90)
    eye.circle(eye_size/2,90)
eye.end_fill()



eye.penup()
eye.goto(100,50)
eye.pendown()
eye.begin_fill()
for loop in range(2):
    eye.circle(eye_size,90)
    eye.circle(eye_size/2,90)
eye.end_fill()
eye.left(45)
eye.hideturtle()

#pupil of the eye
pupil=turtle.Turtle()
pupil.pensize(5)
pupil.pencolor('brown')
pupil.penup()
pupil.goto(-80,50)
pupil.pendown()
pupil.fillcolor('#6b8e23')
pupil.circle(10)
pupil.begin_fill()
pupil.circle(5)
pupil.end_fill()

pupil.penup()
pupil.goto(110,50)
pupil.pendown()
pupil.pendown()
pupil.fillcolor('#6b8e23')
pupil.circle(10)
pupil.begin_fill()
pupil.circle(5)
pupil.end_fill()
pupil.hideturtle()

#for eyebrows

eye_brows=turtle.Turtle()

eye_brows.color('#a0522d')
eye_brows.pensize(10)
eye_brows.penup()
eye_brows.goto(-100,90)
eye_brows.pendown()
eye_brows.forward(25)

eye_brows.penup()
eye_brows.goto(100,90)
eye_brows.pendown()
eye_brows.forward(25)

eye_brows.hideturtle()

#for nose
nose=turtle.Turtle()
nose.pensize(3)
nose.pencolor('brown')
nose.penup()
nose.goto(0,50)
nose.pendown()
nose.circle(-20, steps=3)
nose.hideturtle()

#for smile
smile=turtle.Turtle()
smile.pensize(8)
smile.pencolor('red')
smile.penup()
smile.goto(-100,-70)
smile.pendown()
smile.right(90)
smile.circle(100,180)
smile.hideturtle()

# Vẽ tóc
hair=turtle.Turtle()
hair.pencolor('black')
hair.pensize(5)
hair.penup()
hair.goto(0,0)
hair.pendown()
hair.left(30)
for i in range(7):
    hair.penup()
    hair.forward(200)
    hair.pendown()
    hair.pencolor('black')
    hair.forward(50)
    hair.backward(50)
    hair.penup()
    hair.backward(200)
    hair.pendown()
    hair.left(20)
hair.hideturtle()

#for the chat
Chat=turtle.Turtle()
Chat.pensize(5)
Chat.pencolor('pink')
Chat.speed(5)
Chat.penup()
Chat.goto(250,250) 
Chat.pendown()
Chat.left(60)
Chat.forward(40)
Chat.right(60)


for loop in range(10):
    Chat.circle(25,90)
    Chat.right(120)

Chat.goto(250,250)
Chat.penup()
Chat.right(70)
Chat.forward(80)
Chat.pendown()
Chat.write("Happy Birthday!", align="center", font=("Arial", 14, "normal"))

Chat.hideturtle()

turtle.hideturtle()


turtle.done()