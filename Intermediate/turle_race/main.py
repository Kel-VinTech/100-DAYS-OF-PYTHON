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
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # check if the player crosses the finish line and reset position
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        cars.increase_speed()


    # check for collision wit cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    


screen.exitonclick()