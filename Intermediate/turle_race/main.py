from turtle import Turtle,Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    cars.create_cars()
    cars.move_cars()

    # check if the player crosses the finish line and reset position
    if player.is_at_finish_line():
        player.reset_position()
        cars.increase_speed()




    screen.update()




screen.exitonclick()