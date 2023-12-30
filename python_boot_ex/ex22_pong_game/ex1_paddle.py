# 패들 만들어 움직여보기
# 여러개 패들을 만들기 (클래스화)
import turtle
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, input_x_cor, input_y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(input_x_cor, input_y_cor)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
