import sys
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        print(f"Score before clearing: {self.score}")
        self.score += 1
        self.clear()
        self.debug_log()
        print("Cleared previous score.")
        self.update_scoreboard()
        print("Updated scoreboard with new score.")
        print(f"Score now: {self.score}")
        #print(self.score)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        sys.exit()
       
    def debug_log(self):
        print(f"Current Score: {self.score}")

    def test_clear(self):
        self.clear()