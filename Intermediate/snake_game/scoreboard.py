from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()
    def update_score(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}", align = "center", font={"Arial", 24, "normal"})
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align = "center", font={("Arial", 24, "normal")})

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    def show_score(self):
        self.score += 1
        self.update_score()

        


        