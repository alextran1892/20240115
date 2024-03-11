import math
import turtle

CD = float(input('nhap vao gia tri chieu dai: '))
CR = float(input('nhap vao gia tri chieu rong: '))
 #tinh chu vi
CV = (CD+CR)*2
#tinh dien tich
DT= CD*CR
#display CV va DT
print(CV,DT)

#ve hinh va to mau hinh chu nhat

turtle.pencolor('black')
turtle.fillcolor('pink')
turtle.pensize(5)
# turtle.goto(-100,-100)
turtle.begin_fill()
turtle.forward(CD)
turtle.right(90)
turtle.forward(CR)
turtle.right(90)
turtle.forward(CD)
turtle.right(90)
turtle.forward(CR)
turtle.end_fill()
turtle.done()