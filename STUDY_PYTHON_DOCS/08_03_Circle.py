import turtle
import math

class Circle:
    # ban_kinh = 0
    # hoanh_do = 0
    # tung_do = 0
    
    def __init__(sefl, ban_kinh:float, hoanh_do:int, tung_do:int):
        self.ban_kinh = ban_kinh
        self.hoanh_do = hoanh_do
        self.tung_do = tung_do


    def draw(self):
        t = turtle.Turtle()
        t.Circle(self.ban_kinh)
        t.pensize(15)
        t.pencolor('black')
        t.fillcolor('pink')
        t.begin_fill()
        t.end_fill()
        t.done()
        
a = Circle(100,0,0)
a.draw()
