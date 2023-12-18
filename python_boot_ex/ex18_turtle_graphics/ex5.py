# 터틀 과제 5 스피로 그래프 그리기

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed(10)
screen = t.Screen()
screen.tracer(8, 25)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_colour = (r, g, b)
    return ran_colour


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy.pencolor(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(3.6)
screen.exitonclick()
