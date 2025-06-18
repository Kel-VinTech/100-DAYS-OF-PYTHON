FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260,240)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)
    
    def increase_level(self):
        self.clear()
        self.level +=1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.color("black")
        self.hideturtle()
        
        self.write("GAME OVER", align="center", font=FONT)

        

