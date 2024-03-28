import turtle
import random

# Function to draw a segment of the mountain
def draw_mountain():
    global mountain
    mountain = turtle.Turtle()
    mountain.speed('fastest')
    def draw_mountain_segment(start_point, end_point, deviation):
        # Calculate the midpoint and apply a random deviation
        mid_x = (start_point[0] + end_point[0]) / 2
        mid_y = (start_point[1] + end_point[1]) / 2
        mid_y += random.uniform(0, deviation)

        # If the segment is small enough, draw it, otherwise, subdivide further
        if abs(start_point[0] - end_point[0]) < 2:
            mountain.goto(end_point)
        else:
            mid_point = (mid_x, mid_y)
            draw_mountain_segment(start_point, mid_point, deviation/2)
            draw_mountain_segment(mid_point, end_point, deviation/2)

    # # Setup the screen


    # Initial mountain points and deviation
    start_point = (-150, 333)
    end_point = (250, 333)
    initial_deviation = 150

    # Draw the mountain
    mountain.speed(0)
    mountain.penup()
    mountain.goto(-500,333)
    mountain.pendown()
    mountain.color('#FFF3E0')
    mountain.fillcolor('grey')
    mountain.begin_fill()

    draw_mountain_segment(start_point, end_point, initial_deviation)
    mountain.goto(start_point)
    mountain.end_fill()

    # Finish drawing
    mountain.hideturtle()

  
# draw_mountain()
# turtle.done()