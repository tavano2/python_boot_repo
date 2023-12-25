# 이러한 프로그램을 만들 때 재차 이야기하지만 중요한것은
# 과정을 나눠서 단계별로 처리하자.

# TODO 3. 키보드로 뱀을 컨트롤하는 기능 만들기

# 4번째 부터는 21일 패키지에 도전해보자.
# TODO 4. 화면에 먹이 놓는 기능, 먹이와 부딪혔을때 발생하는 기능
# TODO 5. 점수를 표시하는 점수판 기능
# TODO 6. 뱀이 벽에 부딪혔을 때 게임을 종료하는 기능
# TODO 7. 뱀이 자기 꼬리와 부딪혔을 때 게임을 종료하는 기능

from turtle import Screen
from ex1_snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
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


screen.exitonclick()
