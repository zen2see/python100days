from turtle import Turtle

# Starting positions
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snakesegment:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            asegment = Turtle(shape="square")
            asegment.color('blue')
            asegment.penup()
            asegment.goto(position)
            self.segments.append(asegment)
    
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            newx = self.segments[seg_num -1].xcor()
            newy = self.segments[seg_num -1].ycor()
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