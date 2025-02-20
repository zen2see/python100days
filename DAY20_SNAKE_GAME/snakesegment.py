from turtle import Turtle
import time
import sys

# Starting positions
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snakesegment(Turtle):
    def __init__(self):
        #super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            asegment = Turtle(shape="square")
            asegment.color('blue')
            asegment.penup()
            asegment.goto(position)
            self.segments.append(asegment)

    def add_segment(self, position):
        # Get the position of the last segment
        last_segment = self.segments[-1]
        last_x = last_segment.xcor()
        last_y = last_segment.ycor()
        position = (last_x, last_y)
        # new_segment = Snakesegment()
        # new_segment.goto(last_x, last_y)
        # self.segments.append(new_segment)
        segment = Turtle(shape="square")
        segment.color('blue')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

        # Create a new segment at the last segment's position
        ##new_segment = Snakesegment()
        ##new_segment.goto(last_x, last_y)

        # Add the new segment to the snake
        ##self.segments.append(new_segment)
    def extend(self):
        # Add a segment to the snake at the position of the last segment
        last_segment = self.segments[-1]
        position = last_segment.position()
        self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            newx = self.segments[seg_num -1].xcor()
            newy = self.segments[seg_num -1].ycor()
            if newx >= 280 or newy >= 290 or newx <= -285 or newy <= -280:
                # print(f"Position: x = {newx}, y = {self.segments[seg_num - 1].ycor()}")
                print(f"Position x: = {newx} , Position y: = {newy}")
                time.sleep(2)
                sys.exit()
            self.segments[seg_num].goto(newx, newy)
        self.segments[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)