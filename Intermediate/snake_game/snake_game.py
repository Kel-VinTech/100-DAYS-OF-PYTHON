from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1 ].ycor()

            self.segments[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]




















""" class inheritance
"""


# class Animal:
#     def __init__(self):
#         self.has_eyes = 2

#     def breathe(self):
#         print("Breathing....")
    

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater")
#     def swim(self):
#         print("swimming...")


# nemo = Fish()


# nemo.breathe()
