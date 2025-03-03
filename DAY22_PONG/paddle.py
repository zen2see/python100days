from turtle import Turtle
from scoreboard import Scoreboard

# Starting positions
STARTING_POSITION1 = [(-380, 0)]
STARTING_POSITION2 = [(380, 0)]
MOVE_DIST = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DIST
        if new_y > 300:
            new_y = 300
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DIST
        if new_y <= -300:
            new_y = -300
        self.goto(self.xcor(), new_y)
    