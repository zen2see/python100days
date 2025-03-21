from turtle import Turtle
from scoreboard import Scoreboard

# Starting positions
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snakesegment(Turtle):
    def __init__(self, scoreboard):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.scoreboard = scoreboard

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
        segment = Turtle(shape="square")
        segment.color('blue')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        #scoreboard = Scoreboard()
        for seg_num in range(len(self.segments) -1, 0, -1):
            newx = self.segments[seg_num -1].xcor()
            newy = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(newx, newy)
            if newx >= 280 or newy >= 290 or newx <= -285 or newy <= -280:
                print(f"Position x: = {newx} , Position y: = {newy}")
                self.scoreboard.game_over()
            # Check for collision with the walls # Another methd
            # if self.head.xcor() >= 280 or self.head.ycor() >= 290 or self.head.xcor() <= -285 or self.head.ycor() <= -280:
            # print(f"Position x: = {self.head.xcor()} , Position y: = {self.head.ycor()}")
            # scoreboard.game_over()
            # print(self.head)
        self.head.forward(MOVE_DIST)
        # Check for collision with the tail
        self.detect_collision_with_tail()

    def detect_collision_with_tail(self):
        scoreboard = Scoreboard()
        for segment in self.segments[1:]:  # Skip the head (self.segments[0])
            if self.head.distance(segment) < 10:  # Assuming 10 is the distance for collision
                print("COLLISION with tail")
                print(segment)
                scoreboard.game_over(self)
                
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
    
    