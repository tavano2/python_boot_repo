# importing modules
# basic import
# import turtle
#
# tim = turtle.Turtle()

# from..import
# 별표를 사용하면 모든 기능들을 사용할 수 있다
# 이에 대한 단점은 클래스 또는 메소드가 어디에서 왔는지 파악이 힘들다.
# from turtle import Turtle
#
# timmy = Turtle()
# tom = Turtle()
# terry = Turtle()

# 파이썬 커뮤니티에서 이런 import 문을 찾아보기 힘든 이유가 있다.
# 파악이 힘들기 때문.
# from random import *

#
# choice([1, 2, 3])
#

# alias import
# import turtle as t
#
# t.Turtle()

# installing modules
# import heroes
# 왜 heroes 모듈은 바로 임포트가 안되는 걸까?
# 바로 turtle이 파이썬 표준 라이브러리 패키지에 포함된 모듈이기 때문이고
# 포함된 모듈이 아니라면 설치를 진행하고 사용해야한다.


# 터틀 챌린지 2
import turtle as t

timmy = t.Turtle()
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = t.Screen()
screen.exitonclick()
