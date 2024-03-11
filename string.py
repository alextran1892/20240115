import math
import turtle
R = float(input("Nhap vao ban kinh hinh tron: "))
S = math.pi*R*R
C = 2*math.pi*R
print(S,C)
# VE HINH TRON
turtle.pencolor("black")
turtle.fillcolor("pink")
turtle.begin_fill()
turtle.circle(R)
turtle.end_fill()
turtle.done()