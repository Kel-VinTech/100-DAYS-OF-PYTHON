"""
Learning about instances, state and higher order functions in Python.
"""

from turtle import Turtle, Screen


# tim = Turtle()
# screen = Screen()


# def move_forward():
#     tim.forward(10)


# """"Higher order function takes other functions as their inputs """


# screen.listen()
# # screen.onkey(key = "space",fun = move_forward)




# def move_backward():
#     tim.backward(10)

# def clockwise():
#     new_heading = tim.heading() +10
#     tim.setheading(new_heading)
# def counter_clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear_screen():
#     tim.reset()


# tim.speed("fastest")
# for _ in range(50):
    
#     screen.onkey(key = "w",fun = move_forward)
#     screen.onkey(key = "s", fun = move_backward)
#     screen.onkey(key = "a", fun = counter_clockwise)
#     screen.onkey(key = "d", fun = clockwise)
#     screen.onkey(key = "c", fun = clear_screen)





""" building a turtle


Learning about object state"""


# tim = Turtle()
import random
screen = Screen()
screen.setup(width = 500, height =400)

user_bet = screen.textinput(title = "make your turtle", prompt = "Who would win the race?: ")
print(user_bet)
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
y_positions = [-120, -80,-40, 0 ,40, 80]

all_turtles = []
is_game_on = False




for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_game_on = True   

while is_game_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        if turtle.xcor() >230:
            is_game_on= False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner!")
            # print(f"The {winning_color} turtle is the winner!")
            break # <- stops checking other turtles once a winner is found
        








