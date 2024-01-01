from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.move_position = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        ran_y = random.randint(-200, 300)
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(400, ran_y)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        self.all_car.append(new_car)

    def validation_car(self):
        if self.all_car[-1].xcor() < 360:
            self.create_cars()
        elif self.all_car[-1].xcor() < -350:
            self.all_car[0].clear()
            del self.all_car[0]
            self.create_cars()

    def move(self):
        for car in self.all_car:
            new_x = car.xcor() - self.move_position
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.move_position += MOVE_INCREMENT

