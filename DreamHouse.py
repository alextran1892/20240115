import turtle
from turtle import Turtle
import random as r


#Draw sky
from DreamHouse_Sky import draw_sky
draw_sky()

#Draw mountain
from DreamHouse_Mountain import draw_mountain
draw_mountain()


# Color the sea
from DreamHouse_Sea import color_the_sea
color_the_sea()

#Draw the Sun 2
from DreamHouse_Sun2 import draw_sun_2_with_gradient
draw_sun_2_with_gradient(250)

#Sun
from DreamHouse_Sun import draw_sun_with_gradient
draw_sun_with_gradient(120)
turtle.hideturtle()
turtle.penup()
turtle.goto(-1000,333)
turtle.pendown()
turtle.pencolor('#235284')
turtle.forward(2000)

#Draw cloud
from DreamHouse_Cloud import draw_cloud
draw_cloud()

#Draw Sail Boat
from DreamHouse_Sail_Boat import draw_sail_boat
draw_sail_boat()

#Drawn waves
from DreamHouse_Waves import draw_wave_on_the_sea
draw_wave_on_the_sea()

# Draw flock of bird
from DreamHouse_Birds import draw_birds
draw_birds()

#Draw sand
from DreamHouse_Sand import draw_sand
draw_sand()

#Draw grass
from DreamHouse_Grass import draw_grass
draw_grass()

#Draw Umbrella
from DreamHouse_Umbrella import draw_umbrella
draw_umbrella()

#Draw rock path
from DreamHouse_Rock_Path import draw_rock_path
draw_rock_path()

#Draw moving turtles
from DreamHouse_Turtles import draw_turtle_on_the_sea
draw_turtle_on_the_sea()

turtle.done()


