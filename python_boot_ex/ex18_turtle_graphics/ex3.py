# 터틀 챌린지3
import turtle
import turtle as t
import random


turn = 3
CIRCLE = 360
timmy = turtle.Turtle()
timmy.shape("arrow")
colours = ["cornflower blue", "spring green", "yellow", "green", "firebrick", "navajo white", "orange", "powder blue",
           "medium orchid", "seashell"]

while turn < 10:
    timmy.color(random.choice(colours))
    for i in range(turn):
        if turn == i:
            timmy.forward(100)
        else:
            timmy.forward(100)
            timmy.right(CIRCLE / turn)
    turn += 1


screen = t.Screen()
screen.exitonclick()
