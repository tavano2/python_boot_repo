from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_write(0, 0)

    def score_write(self, l_num, r_num):
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.penup()
        self.score_update(l_num, r_num)

    def score_update(self, l_num, r_num):
        self.clear()
        self.write(f"Score: {l_num} : {r_num}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
