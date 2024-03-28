import turtle
from turtle import Screen, Turtle
import random as r
wave_color_list = ['#235284', '#3271a5','#3982b8', '#4194cb', '#46a2da','#58afdd', '#6abce2', '#8dcfec', '#b8e2f4']
#Waves
def draw_wave_on_the_sea():
    all_waves = []
    global run
    run = True
    y_position = [290,275,260,245,230,215,200,185,170,155,140,125,110,95,80,65,50,35,20,5]
    for wave in range(0,20):
        waves = turtle.Turtle(shape="turtle")
        waves.penup()
        waves.goto(x=-1000, y=y_position[wave])
        waves.speed(100)
        waves.pensize(1)
        waves.color(wave_color_list[r.randint(0,len(wave_color_list)-1)])
        all_waves.append(waves)

    def draw_wave(waves):
        global run
        for wave in waves:
            #Cài đặt màu ngẫu nhiên cho mỗi bước 
            wave.pencolor(wave_color_list[r.randint(0,len(wave_color_list)-1)])
            down = r.randint(10,40)
            up = r.randint(10,40)
            wave.pendown()
            #Rùa tiến lên phía trước với giá trị ngẫu nhiên có để lại nét vẽ
            wave.circle(down/2,90)
            wave.circle(-down/2,-90)
            wave.right(180)
            wave.penup()
            #Rùa tiến về phía trước với giá trị ngầu nhiên không để lại nét vẽ
            wave.forward(up)
            if wave.xcor() > 1000:
                run = False
    while run:
        draw_wave(all_waves)
