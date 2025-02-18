import time
from turtle import Turtle, Screen
from snakesegment import Snakesegment
import random

"""
Pointer: ((15,0),(0,25),(-15,0),(0,3))
Noel Star: ((0,20),(-5,5),(-20,0),(-5,-5),(0,-20),(5,-5),(20,0),(5,5))
X: ((15,15),(-15,-15),(0,0),(15,-15),(-15,15),(0,0))
Cross: ((-7.5,-15),(7.5,-15),(7.5,-7.5),(15,-7.5),(15,7.5),(7.5,7.5),(7.5,15),(-7.5,15),(-7.5,7.5),(-15,7.5),(-15,-7.5),(-7.5,-7.5))
Right Triangle: ((20,0),(0,-20),(0,0))
Arrow: ((-15,7.5),(-10,0),(-15,-7.5),(5,-7.5),(15,0),(5,7.5))
Parallelogram: ((-30,20),(-40,-20),(30,-20),(40,20)) 
Rhombus: ((0,-20),(-10,0),(0,20),(10,0))
Trapezoid: ((-20,20),(20,20),(30,0),(-30,0))
Pentagon: ((-5,10),(-10,0),(-5,-10),(5,-10),(10,0),(5,10))
Hexagon: ((-10,20),(-20,0),(-10,-20),(10,-20),(20,0),(10,20))
Octagon: ((-10,20),(10,20),(20,10),(20,-10),(10,-20),(-10,-20),(-20,-10),(-20,10))
"""

t = Turtle(shape="square")
t.shapesize(1,1)

snake = Snakesegment()

# Draw a rectangle
# def rectangle(width, height):
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)

# # Draw Segments
# def create_segments(start_position):
#     segments = [] 
#     for position in start_position:
#         segment = Turtle(shape="square")
#         segment.color('blue')
#         segment.penup()
#         segment.goto(position)
#         segments.append(segment)
#     return segments

# def move(segments):
#    for seg_num in range(len(segments) -1, 0, -1):
#            newx = segments[seg_num -1].xcor()
#            newy = segments[seg_num -1].ycor()
#            segments[seg_num].goto(newx, newy)
#    segments[0].forward(20)

def main():
    """
    register_shape() function. The first argument is what you will name the shape; 'rectangle',
    in this case. The second argument is the coordinates, so save them as a variable.
    """
    rectCors = ((-20,10),(20,10),(20,-10),(-20,-10))
    #t.register_shape('rectangle',rectCors);
    #t = Turtle(shape='square')
    # squareCors = (20,20)
    # t.register_shape('square', squareCors)
    screen = Screen()
    screen.title('Snake Game')
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=600, height=600)

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Set the dimensions of the rectangle
    rectangle_width = 200
    rectangle_height = 100

    # Hide the turtle
    t.hideturtle()

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
            
    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()