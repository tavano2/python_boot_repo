# 점수를 표시하는 점수판 기능
from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_write(0)

    def score_write(self, num):
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.penup()
        self.score_update(num)

    def score_update(self, num):
        self.clear()
        self.write(f"Score: {num}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)