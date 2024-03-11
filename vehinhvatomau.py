import turtle
Turtle_size = input()
shapeInput = input('circle, turtle, fish and square, what is your favorite shape?: ')
if shapeInput == 'circle' or shapeInput == 'square' or shapeInput == 'turtle' or shapeInput == 'fish' :
    colorInput = input('what color will it be?, yellow, red or blue?: ')
    if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue':
        wn = turtle.Screen()
        wn.bgcolor('black')
        wn.title('your shape')
        

        displayShape = turtle.Turtle()
        displayShape.shape(shapeInput)
        displayShape.color(colorInput)

        turtle.done()
    else:
        print('Sorry, I dont have this color')
else:
    print('Sorry, I dont have this shape')
