import time, sys
from turtle import Turtle

LALIGNMENT = "left"
ALIGNMENT = "center"
RALIGNMENT = "right"
FONT = ("Courier", 20, "normal")
FONT2 = ("Courier", 10, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280, 260)
        self.score = 0
        self.hiscore = 0
        self.level = 1
        try:
           with open("snakedata.txt") as data:
               self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Score: {self.score}", align=LALIGNMENT, font=FONT)
        self.goto(280, 260)
        self.write(f"Hi-Score: {self.high_score}", align=RALIGNMENT, font=FONT)
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open("snakedata.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 
        self.level = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        if self.score >= self.high_score:
            self.high_score = self.score
        self.update_scoreboard() 

    def game_over(self):
        self.reset()
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        time.sleep(3)
        sys.exit()
    
