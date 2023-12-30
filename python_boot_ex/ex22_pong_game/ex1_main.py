from turtle import Screen
from ex1_paddle import Paddle
from ex1_ball import Ball
from ex1_scoreboard import Scoreboard
from time import sleep


# 화면 만들기
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My PingPong Game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)

screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

ball = Ball()
scoreboard = Scoreboard()
game_is_on = True
score_r = 0
score_l = 0

while game_is_on:
    sleep(ball.move_speed)
    screen.update()

    # 공이 벽과 부딪혀 튕겨내게 만들기
    if ball.ycor() > 270:
        ball.bounce()
    elif ball.ycor() < -270:
        ball.bounce()

    # 패들에 부딪혔는지 감지하여 튕겨내게 만들기
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.reverse()

    # 패들이 공을 놓치면 공을 리셋하는 기능 만들기
    # 점수판 기능 만들기
    if ball.xcor() > 380:
        score_l += 1
        ball.reset_ball()
    elif ball.xcor() < -380:
        score_r += 1
        ball.reset_ball()

    scoreboard.score_update(score_l, score_r)

    ball.move()


screen.exitonclick()
