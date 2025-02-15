from turtle import Turtle, Screen
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

# Draw a rectangle
def rectangle(width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

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

    #Starting positions
    start_position = [(0,0), (-20,0), (-40,0)]

    for position in start_position:
        segment = t.clone
        # segment.color('blue')
        segment.goto(position)
    #screen.register_shape('rectangle', rectCors)

    # Set the dimensions of the rectangle
    rectangle_width = 200
    rectangle_height = 100

    # Position the turtle
    t.penup()
    t.color("white")
    t.fillcolor("grey") # Set the fill color
    t.goto(-rectangle_width//2, -rectangle_height//2)  # Center the rectangle
    t.pendown()

    # Draw the rectangle
    t.begin_fill()
    rectangle(rectangle_width, rectangle_height)
    t.end_fill()

    # Hide the turtle
    t.hideturtle()

    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()