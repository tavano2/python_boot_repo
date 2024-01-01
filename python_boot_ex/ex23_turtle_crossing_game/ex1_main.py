import time
from turtle import Screen
from ex1_player import Player
from ex1_car_manager import CarManager
from ex1_scoreboard import Scoreboard

"""
정답 솔루션과 나의 첫 코딩 차이점
    1. 나는 카 매니저 기능을 정확하게 이해하지 못하고 main.py에 매니저 기능을 작성했다.
        - 카매니저 내부 배열로 차들을 생성하는 로직
        - 레벨업시 차들이 빨라지는 로직
    2. 차를 생성시 솔루션은 1~6 랜덤 난수를 만들어 해당 난수가 1과 일치할 때 생성했다. 1/6 확률로 생성
        - 나는 x축 기준으로 일정 이상 갔을시 생성
"""


screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(key="w", fun=player.move_up)
screen.onkeypress(key="w", fun=player.move_up)

score = Scoreboard()
car_manager = CarManager()
car_manager.create_cars()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.validation_car()
    car_manager.move()

    for car in car_manager.all_car:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    if player.is_finished():
        player.level_up()
        score.level_up()
        car_manager.level_up()

screen.exitonclick()
