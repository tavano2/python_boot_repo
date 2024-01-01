# 점수를 표시하는 점수판 기능
from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.score_write(self.score)

    def score_write(self, num):
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.penup()
        if num != 0:
            self.score = num
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_update()

    def read_high_score(self):
        with open("snake_data.txt", mode="r") as data:
            self.high_score = int(data.read())

    def write_high_score(self):
        with open("snake_data.txt", mode="w") as data:
            save_data = str(self.high_score)
            data.write(save_data)

