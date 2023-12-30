# 공을 만들어 화면에서 계속 움직이게 하기

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        move_x = self.xcor() + self.move_x
        move_y = self.ycor() + self.move_y
        self.goto(move_x, move_y)

    def bounce(self):
        self.move_y *= -1

    def reverse(self):
        self.move_speed -= 0.01
        self.move_x *= -1

    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0, 0)
