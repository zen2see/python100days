import time, sys
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.getscreen().update()
        time.sleep(5)
        sys.exit()

