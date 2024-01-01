from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-350, 220)
        self.level = 1
        self.write_score(self.level)

    def write_score(self, level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_score(self.level)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

