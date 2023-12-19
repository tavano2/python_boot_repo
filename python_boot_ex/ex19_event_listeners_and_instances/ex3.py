import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

"""
지금까지는 하나의 객체만 생성시켜 작용했다면
여러개의 객체를 생성시켜 각 객체마다 독립적으로 활용하는 것을 공부해보자.
이렇게 하나의 클래스를 n개의 객체로 생성시킬 수 있으며, 이 객체를 인스턴스라 부른다.

그리고 각 객체가 어느 한 순간에 각기 다른 속성을 지닐 수 있으며
각기 다른 메소르를 수행할 수 있다는 사실을 객체의 상태라고 부른다.

"""
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
numbering = 0
PLUS_Y = 50
VAL_X = -225.00
val_y = -120.00
is_race_on = False

for item in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(item)
    new_turtle.penup()
    if numbering == 0:
        new_turtle.goto(x=VAL_X, y=val_y)
    else:
        val_y += PLUS_Y
        new_turtle.goto(x=VAL_X, y=val_y)
    all_turtles.append(new_turtle)
    numbering += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for one_turtle in all_turtles:
        if one_turtle.xcor() > 230:
            is_race_on = False
            winning_color = one_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle has winner!")
            else:
                print(f"You've lost! The {winning_color} turtle has winner!")

        ran_num = random.randint(0, 10)
        one_turtle.forward(ran_num)

"""
파이썬은 내부적으로 중첩 객체를 생성시켰을 시 다른 메모리 주소를 참조하게 함으로써
주소를 덮어쓰지 않고 for문 생성시 여러개 객체가 생성됨을 알 수 있다.
하지만 여기서 참조하지 않는다면, 프로그램 종료시 객체가 휘발됨을 주의하자.
"""

screen.exitonclick()
