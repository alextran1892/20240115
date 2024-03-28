import turtle
import random

# Function to draw a rock
def draw_rock_path():
    x = -90
    y = -502
    rock_size = 80
    for i in range(5):
        rock = turtle.Turtle()
        rock.speed('fastest')
        rock.hideturtle()
        rock.color('#348C31') #Grass color
        rock.pensize(5)
        rock.penup()
        rock.goto(x,y)
        rock.pendown()
        for k in range (20):
            rock.fillcolor('#CACAC8') #Light grey color
            rock.begin_fill()
            rock.circle(rock_size,90)
            rock.circle(rock_size/2,90)
            rock.end_fill()
        x+=30
        y+=70
        rock_size-=5

# draw_rock_path()
# turtle.hideturtle()
# turtle.done()
