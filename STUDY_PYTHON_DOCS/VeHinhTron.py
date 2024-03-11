import turtle
#kích thước viền hình tròn
turtle.pensize(10)
#màu sắc viền hình tròn
turtle.pencolor('#808080')
#tùy chỉnh điểm bắt đầu vẽ hình tròn
turtle.Turtle().goto(-200,200)
#màu nền hình tròn
turtle.fillcolor('#ff69b4')
turtle.begin_fill()
#bán kính hình tròn 100
turtle.circle(200)
turtle.end_fill()
turtle.done()