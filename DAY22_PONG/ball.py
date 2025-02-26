from turtle import Turtle
import random
from scoreboard import Scoreboard

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def move(self):
        scoreboard = Scoreboard()
        for seg_num in range(len(self.segments) -1, 0, -1):
            newx = self.segments[seg_num -1].xcor()
            newy = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(newx, newy)
            if newx >= 280 or newy >= 290 or newx <= -285 or newy <= -280:
                print(f"Position x: = {newx} , Position y: = {newy}")
                scoreboard.game_over()
            # Check for collision with the walls # Another methd
            # if self.head.xcor() >= 280 or self.head.ycor() >= 290 or self.head.xcor() <= -285 or self.head.ycor() <= -280:
            # print(f"Position x: = {self.head.xcor()} , Position y: = {self.head.ycor()}")
            # scoreboard.game_over()
            # print(self.head)
        self.head.forward(MOVE_DIST)
        # Check for collision with the tail
        self.detect_collision_with_tail()