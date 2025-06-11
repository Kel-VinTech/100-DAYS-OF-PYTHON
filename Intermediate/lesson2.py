"""
Learning about object oriented programming
# it takes attributes and functions
"""

# class User:


#     """ initializing an object using the init
#     """
    
#     def __init__(self,username):
#         # use the dot notation to create an attribute for it's object.
#         self.username = username
#         self.follower = 0
#         self.following = 0
#     def follow(self, user):
#         user.following += 1
#         self.following += 1


# user_1 = User("David")
# user_2 = User("Angel")

# user_1.follow(user_2)

# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)

""" Learning about the turtle module
This module is used to create graphics and drawings in Python."""

# from turtle import Screen
import turtle as t
import random


tinny = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b =  random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# colors = [ "blue", "red", "green", "black"]


# for _ in range(15):
#     tinny.forward(10)
#     tinny.penup()
#     tinny.forward(10)
#     tinny.pendown

# def draw_shape(num_sides):
#     angles = 360/ num_sides
#     for _ in range(num_sides):
#         tinny.forward(100)
#         tinny.right(angles)
# for shape_side in range(3, 11):
#     draw_shape(shape_side)
#     tinny.color(random_color())




# tinny.pensize(10)
# tinny.speed("fastest")
# colors = [ "blue", "red", "green", "black"]
# directions = [0, 90 , 180 , 270]

# for _ in range(200):
#     tinny.setheading(random.choice(directions))
#     tinny.forward(30)
#     tinny.color(random_color())
    

# tinny.speed("fastest")
# def draw_sprial(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tinny.color(random_color())
#         tinny.setheading(tinny.heading() + size_of_gap)
#         tinny.circle(100)


# draw_sprial(5)




























screen = t.Screen()
screen.exitonclick()


