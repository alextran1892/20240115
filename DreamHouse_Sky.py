from turtle import Turtle
def draw_sky():
    # COLOR = (0.86328, 0.47656, 0.11250)
    # TARGET = (0.2314884, 0.3769016, 0.5629210)

    COLOR = (0.00000001, 0.80156, 0.88100)
    TARGET = (0.2314884, 0.3769016, 0.4629210)


    deltas = [(hue - COLOR[index]) / 167 for index, hue in enumerate(TARGET)]

    sky = Turtle()
    sky.color(COLOR)
    sky.speed('fastest')
    sky.penup()
    sky.goto(-1000, 500)
    sky.pendown()

    direction = 1

    for distance, y in enumerate(range(500, 333, -1)):

        sky.forward(2000 * direction)
        sky.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
        sky.sety(y)

        direction *= -1