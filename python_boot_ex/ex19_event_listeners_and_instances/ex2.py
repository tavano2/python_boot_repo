# make a etch-a-Sketch

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


def move_down():
    tim.backward(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=move_down, key="s")
screen.onkey(fun=clear, key="c")
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=move_right, key="d")
screen.onkeypress(fun=move_down, key="s")


screen.exitonclick()
