from turtle import Turtle
import random
from scoreboard import Scoreboard

# STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 2
FINISH_LINE_Y = 350

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.color("green")
        self.penup()
        self.move_speed = .1
        
    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(400, -350)
        self.move_speed = 2
        

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor() )