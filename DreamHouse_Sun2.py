import turtle
import colorsys

sun_color_list = ['#FFF3E0','#FFE0B2','#FFCC80','#FFB74D','#FFA726','#FF9800','#FB8000','#F57000','#EF6C00','#E65100']

def draw_sun_2_with_gradient(radius):
    sun2 = turtle.Turtle()
    sun2.hideturtle()
    sun2.speed('fastest')
    sun2.width(2)
    sun2.penup()
    sun2.goto(600,100)
    sun2.left(90)
    sun2.pendown()
   
    # Set the start and end colors for the gradient
    start_rgb = (106, 188, 226)    #  light shade of cyan
    end_rgb = (255, 102, 0)    # Deep orange(255, 204, 0)  # Bright yellow
    # Convert RGB to color values sun2 understands (0 to 1)
    start_color = tuple(c / 255 for c in start_rgb)
    end_color = tuple(c / 255 for c in end_rgb)

    # Function to interpolate between two colors
    def interpolate(start_color, end_color, t):
        return (start_color[0] + (end_color[0] - start_color[0]) * t,
                start_color[1] + (end_color[1] - start_color[1]) * t,
                start_color[2] + (end_color[2] - start_color[2]) * t)
    # Draw the sun2 with gradient
    for i in range(radius):
        color = interpolate(start_color, end_color, i / radius)
        sun2.color(color)
        sun2.dot(2 * (radius - i))
        sun2.up()
        sun2.forward(1)
        sun2.down()
# def draw_sun():
#     sun = turtle.Turtle()
#     sun.speed(100)
#     sun.pensize(1)
#     sun.penup()
#     sun.goto(400,333)
#     sun.right(90)
#     sun.pendown()
#     r = 300
#     x = 350
#     for i in range (10):
#         sun.pencolor(sun_color_list[i])
#         sun.fillcolor(sun_color_list[i])
#         sun.begin_fill()
#         sun.circle(r,-180)
#         sun.penup()
#         sun.goto(x,333)
#         sun.right(180)
#         sun.pendown()
#         r-=30
#         x+=30
#         sun.end_fill()

# draw_sun_2_with_gradient(300)
# turtle.done()