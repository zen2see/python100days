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
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 300)
        self.write(f"Score: {self.lscore}", align=ALIGNMENT, font=FONT)
        self.goto(300, 300)
        self.write(f"Score: {self.rscore}", align=RALIGNMENT, font=FONT)
   
    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()

    def r_point(self):
        self.rscore += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))