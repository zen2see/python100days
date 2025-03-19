import time, sys
from turtle import Turtle

LALIGNMENT = "left"
ALIGNMENT = "center"
RALIGNMENT = "right"
FONT = ("Courier", 18, "normal")
FONT2 = ("Courier", 14, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 320)
        self.score = 0
        self.hiscore = 0
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-330, 320)
        self.write(f"Score: { self.score}", align=LALIGNMENT, font=FONT)
        self.goto(0, 320)
        self.write(f"Level: { self.level}", align=ALIGNMENT, font=FONT2)
        self.goto(330, 320)
        self.write(f"Hi-Score: {self.hiscore}", align=RALIGNMENT, font=FONT)
   
    def point(self):
        self.score += 1
        if self.score >= self.hiscore:
            self.hiscore = self.score
        self.update_scoreboard()    

    def levelup(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()    

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        # self.update_scoreboard()  # Update high score when game over


        

    