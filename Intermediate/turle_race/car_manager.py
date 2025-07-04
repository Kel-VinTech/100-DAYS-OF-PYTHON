from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE
        
        
    def create_cars(self):    
        # This will create a new car with a 1 in 6 chance
            if random.randint(1, 6) == 1:
                new_car = Turtle("square")
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.goto(300, random.randint(-250, 250))
                self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
        