from turtle import Turtle,Screen
from pong_paddle import Paddle
from pong_ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width= 800, height=600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on =True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # collision with r_paddle


screen.exitonclick()

