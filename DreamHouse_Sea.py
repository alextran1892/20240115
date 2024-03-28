from turtle import Screen, Turtle

    #Color the see gradient

def color_the_sea():
    #Color the see gradient
    COLOR = (0.2314884, 0.3769016, 0.4629210)
    TARGET = (0.00000001, 0.80156, 0.88100)

    # COLOR = (0.137254902,0.321568627,0.517647059)
    # TARGET = (0.721568627, 0.88627451, 0.956862745)


    deltas = [(hue - COLOR[index]) / 333 for index, hue in enumerate(TARGET)]

    turtle = Turtle()
    turtle.color(COLOR)
    turtle.speed('fastest')

    turtle.penup()
    turtle.goto(-1000, 333)
    turtle.pendown()

    direction = 1

    for distance, y in enumerate(range(333, 0, -1)):

        turtle.forward(2000 * direction)
        turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        turtle.sety(y)

        direction *= -1
  


# #Tô màu biển
# pen.penup()
# pen.goto(-1000,333)
# pen.pendown()
# pen.speed(100)
# for k in range(9):
#     for i in range (2):
#         pen.pencolor(wave_color_list[k])
#         pen.fillcolor(wave_color_list[k])
#         pen.begin_fill()
#         pen.forward(2000)
#         pen.right(90)
#         pen.forward(37)
#         pen.right(90)
#         pen.end_fill()
#     pen.right(90)
#     pen.forward(37)
#     pen.left(90)
