import turtle as t
import random
# import colorgram
#
# LEN = 30
# colors = colorgram.extract("spot.jpg", LEN)
# colors_arr = []
# for i in range(LEN):
#     colors_arr.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

color_list = [(238, 229, 234), (227, 235, 230), (196, 162, 106), (67, 90, 125), (141, 168, 188), (134, 91, 51), (216, 206, 127), (145, 63, 87), (32, 39, 64), (188, 143, 159), (75, 15, 33), (129, 28, 54), (137, 182, 145), (163, 154, 54), (43, 55, 102), (177, 97, 109), (52, 37, 28), (62, 120, 106), (101, 123, 165), (219, 176, 186), (164, 202, 210), (86, 146, 157), (92, 150, 101), (185, 106, 83), (174, 206, 170), (77, 68, 41), (180, 189, 211), (35, 58, 57)]

MOVE_UP = 50
val_y = -235

timmy = t.Turtle()
screen = t.Screen()
screen.setup(width=550, height=550)
screen.tracer(8, 25)
t.colormode(255)

timmy.hideturtle()
timmy.penup()
timmy.goto(-260.0, -235.0)


def draw_pen():
    for i in range(10):
        if i == 0:
            timmy.forward(25)
        else:
            timmy.forward(50)
        timmy.dot(20, random.choice(color_list))


for _ in range(10):
    draw_pen()
    val_y += MOVE_UP
    timmy.goto(-260.0, val_y)

screen.exitonclick()


"""
솔루션 정답은 나보다 좀 더 복잡한 형식으로 진행했다.
나는 절대 위치 경로를 매번 변경한 것인데, 솔루션은 지그재그로 펜을 옮겨가면서
점을 그리는 위치를 특정했다.
"""