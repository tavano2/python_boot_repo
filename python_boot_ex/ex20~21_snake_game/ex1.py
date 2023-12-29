# 이러한 프로그램을 만들 때 재차 이야기하지만 중요한것은
# 과정을 나눠서 단계별로 처리하자.

# 4번째 부터는 21일 패키지에 도전해보자.

from turtle import Screen
from ex1_snake import Snake
from ex1_food import Food
from ex1_scoreboard import Scoreboard
import time

TURTLE_SCORE = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # 먹이와 부딪혔을때 발생하는 기능
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        TURTLE_SCORE += 1
        scoreboard.score_write(TURTLE_SCORE)

    # 뱀이 벽에 부딪혔을 때 게임을 종료하는 기능
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # 뱀이 자기 꼬리와 부딪혔을 때 게임을 종료하는 기능
    # 슬라이싱을 이용해 개선해보기
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
