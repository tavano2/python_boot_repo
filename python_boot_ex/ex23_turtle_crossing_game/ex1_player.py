from turtle import Turtle


STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.tt_start_line()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def level_up(self):
        self.tt_start_line()

    def tt_start_line(self):
        self.goto(STARTING_POSITION)

    def is_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
