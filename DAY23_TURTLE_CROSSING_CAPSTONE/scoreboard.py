import time, sys
from turtle import Turtle

ALIGNMENT = "center"
RALIGNMENT = "right"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.hiscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 300)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(300, 300)
        self.write(f"Hi Score: {self.hiscore}", align=RALIGNMENT, font=FONT)
   
    def point(self):
        self.score += 1
        self.update_scoreboard()

    def hipoint(self):
        if self.score > self.hiscore:
            self.hiscore = self.score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        self.hipoint()  # Update high score when game over