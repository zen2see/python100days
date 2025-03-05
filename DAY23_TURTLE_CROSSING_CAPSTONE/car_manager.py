from turtle import Turtle
import random


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=random.randint(2,10), stretch_len=1)
        self.goto(0, random.randint(-350, 350))
        self.move_speed = (random.randint(1,10))
        self.x_move = MOVE_INCREMENT
        self.y_move = (random.randint(-400,400))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
