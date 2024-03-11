from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # detect collision with paddles
    if ball.xcor() > 340 and ball.distance(r_paddle) < 40 and ball.x_move > 0 \
            or ball.xcor() < -340 and ball.distance(l_paddle) < 40 and ball.x_move < 0:
        ball.paddle_bounce()

    # detect misses
    elif ball.xcor() > 400:
        scoreboard.increase_l_score()
        scoreboard.report_score()
        ball.reset()
    elif ball.xcor() < -400:
        scoreboard.increase_r_score()
        scoreboard.report_score()
        ball.reset()


screen.exitonclick()
