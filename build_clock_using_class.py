import turtle
import time

#Xây dựng lớp clock
class Clock:
    #Thuộc tính của clock
    # def __init__(self, hour, minute, second, r, heart):
    #     self.hour = hour
    #     self.minute = minute
    #     self.second = second
    #     self.r = r #Bán kính đồng hồ
    #     self.heart = heart 

    # Hàm vẽ mặt của đồng hồ, các vạch chia của đồng hồ

    screen = turtle.Screen()
    screen.bgcolor('gray')

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.pencolor('black')
    t.pensize(3)
    t.speed(100)
    t.fillcolor('pink')
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    t.penup()
    t.home()
    x = 6 
    for i in range(12):
        t.forward(180)
        t.pendown()
        t.forward(10)
        t.penup()
        t.home()
        t.right(x)
        x+=6
        for k in range(4):
            t.forward(185)
            t.pendown()
            t.forward(5)
            t.penup()
            t.home()
            t.right(x)
            x+=6

    # Hàm vẽ tim đồng hồ

    clock_heart = turtle.Turtle()
    clock_heart.pencolor('black')
    clock_heart.pensize(3)
    clock_heart.hideturtle()
    clock_heart.penup()
    clock_heart.goto(0, 0)
    clock_heart.pendown()
    clock_heart.circle(3)
        
    
    # Hàm vẽ các kim giờ, phút, giây

    hour_hand = turtle.Turtle()
    hour_hand.pencolor('yellow')
    hour_hand.pensize(4)
    hour_hand.hideturtle()

    
    #Hàm vẽ kim phút

    minute_hand = turtle.Turtle()
    minute_hand.pencolor('black')
    minute_hand.pensize(3)
    minute_hand.hideturtle()


        
    #Hàm vẽ kim giây
    second_hand = turtle.Turtle()
    second_hand.pencolor('red')
    second_hand.pensize(2)
    second_hand.hideturtle()

        
    #Cập nhật kim đồng hồ
    def update_current_time(self):
        
        for i in range 1:
            current_time = time.localtime()
            hour = current_time.tm_hour
            minute = current_time.tm_min
            second = current_time.tm_sec

            #Tính góc cho các kim đồng hồ
            angle_hour_hand = (hour % 12) * 30 + (minute/60) * 30
            angle_minute_hand = minute *6 + (second / 60) * 6
            angle_second_hand = second * 6
            self.second_hand.setheading(90 - angle_second_hand)
            #Đặt vị trí cho kim đồng hồ
            self.second_hand.forward(170)
            self.second_hand.backward(170)
            time.sleep(0.3)
            self.second_hand.clear()
            
            self.minute_hand.setheading(90 - angle_minute_hand)
            self.minute_hand.forward(150)
            self.minute_hand.backward(150)
            # self.minute_hand.clear()

            self.hour_hand.setheading(90 - angle_hour_hand)
            self.hour_hand.forward(100)
            self.hour_hand.backward(100)
            # time.sleep(3600)
            # self.hour_hand.clear()




            #Cập nhật màn hình
            self.screen.update()



        

c = Clock()
c.update_current_time()
turtle.done()