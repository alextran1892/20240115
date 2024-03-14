
import turtle
from random import randint
turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor('pink')

elip = turtle.Turtle()

elip.penup()
elip.home()
elip.right(45)
elip.pendown()

#khai bao bien elip size kich thuoc mat
r = 100
count = 0
while True:
    for loop in range(2):
        elip.color(randint(0,255),randint(0, 255),randint(0, 255))
        elip.pensize(3)
        elip.speed(0.5)
        elip.circle(r,90)
        elip.circle(r/2,90)
    elip.left(10)
    count +=1
    if count == 36:
        break
    

turtle.done()