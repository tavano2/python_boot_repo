# 터틀 챌린지 4 random walk

import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

angle_arr = [0, 90, 180, 270]
colours = ["cornflower blue", "spring green", "yellow", "green", "firebrick", "navajo white", "orange", "powder blue",
           "medium orchid", "seashell"]
timmy.shape("classic")
timmy.pensize(10)
timmy.speed(3)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ran_colour = (r, g, b)
    return ran_colour


for _ in range(200):
    timmy.pencolor(random_colour())
    timmy.forward(50)
    timmy.setheading(random.choice(angle_arr))

# 튜플과 리스트의 차이점은 무엇일까?
"""
튜플은 돌에 새기는것과 같다. 즉 값을 변경할 수 없다.
튜플은 아이템을 제거할 수도 없는 즉 상수 자료구조이다.
그럼 튜플을 왜 사용할까?
웹사이트와 같이 색상 구성표를 일정하게 유지하고자 하는 리스트를 생성하고
누군가가 그 리스트를 실수로 변경하기를 원하지 않는다고 생각할 때 유용하게 사용된다.
"""


