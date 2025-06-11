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

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b =  random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color

color_list = [
(236, 158, 48), (153, 63, 64), (199, 192, 119), (35, 88, 160), (182, 212, 242),
(57, 45, 37), (250, 229, 139), (71, 136, 167), (98, 56, 124), (101, 153, 51),
(243, 56, 63), (60, 114, 107), (209, 200, 192), (173, 223, 183), (251, 210, 55),
(187, 75, 154), (174, 105, 49), (137, 132, 53), (109, 71, 166), (43, 53, 86),
(168, 178, 230), (56, 180, 172), (238, 184, 183), (212, 91, 36), (58, 76, 30),
(68, 89, 87), (243, 121, 159), (243, 92, 33), (142, 204, 80), (221, 147, 79)
 ]

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
#         tinny.color(random.choice(color_list))
#         tinny.setheading(tinny.heading() + size_of_gap)
#         tinny.circle(100)


# draw_sprial(5)



tinny.speed("fastest")
tinny.penup()
tinny.hideturtle()
tinny.setheading(225)
tinny.forward(300)
tinny.setheading(0)
number_of_dot = 101


for dot_count in range(1,number_of_dot):
    tinny.dot(20,random.choice(color_list))
    tinny.forward(50)

    if dot_count % 10 == 0:
        tinny.setheading(90)
        tinny.forward(50)
        tinny.setheading(180)
        tinny.forward(500)
        tinny.setheading(0)
        

















screen = t.Screen()
screen.exitonclick()


