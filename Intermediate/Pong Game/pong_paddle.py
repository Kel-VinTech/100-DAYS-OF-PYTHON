from turtle import Turtle,Screen



class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.speed("fastest")  # Set the speed to the fastest for immediate response

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 30  # You can also increase the movement here
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)





