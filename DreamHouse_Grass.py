import turtle
def draw_grass():
    COLOR = (0.57254902,0.811764706,0.501960784) 
    TARGET = (0.305882353,0.619607843,0.439215686)

    deltas = [(hue - COLOR[index]) / 367 for index, hue in enumerate(TARGET)]

    grass = turtle.Turtle()
    grass.color(COLOR)
    grass.speed('fastest')
    grass.penup()
    grass.goto(-1000, -133)
    grass.pendown()

    direction = 1

    for distance, y in enumerate(range(-133, -500, -1)):

        grass.forward(2000 * direction)
        grass.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        grass.sety(y)
        direction *= -1
    
# draw_grass()
# turtle.done()
