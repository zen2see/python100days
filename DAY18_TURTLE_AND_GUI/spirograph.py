from os import system, name
import time, random
from turtle import Turtle, Screen

# docs.python.org/3.3/library/turtle.html
# docs.python.org/3/library/tkinter.html
# You’ll need  Tk interface package installed  
# Running python -m tkinter should demonstrating a simple Tk interface
# tcl.tk/man/tcl8.4/TkCmd/colors.htm
# cs111.wellesley.edu/labs/lab01/colors
# tinket.io/docs/colors

# NOTES
# home() = center of screen
# turtles state position() | pos()
# pos() = x-y coordinates
# abs(pos()) < 1 is a good way to know when the turtle is back at its home position.
# clearscreen()
# fillcolor('green')
# abs(pos()) < 1 is a good way to know when the turtle is back at its home position.
# forward(100) fd() move forward # left(120) turns left 120 degrees
# up(), down() determines whether the line will be drawin
# begin_fill() filing can be turned off
# setpos(60, 30) Move turtle to an abs pos. If the pen is down, draw line. no change of orientation.
# teleport(60, 30) Move turtle to an absolute position. Unlike goto(x, y), a line will not be drawn
# setx(x), sety(y), setheading(to_angle) seth 0-east 90-north 180-west 270-south
# circle(radius, extent=None, steps=None) turtle.circle(120, 180)  # draw a semicircle
# turtle.stamp()
# Stamp a copy of the turtle shape onto the canvas at the current turtle position. 
# Return a stamp_id for that stamp, which can be used to delete it by calling clearstamp(stamp_id).



# RANDOM COLOUR USING RGB
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgbcolor = (r,b,g)
    return rgbcolor

def draw_spirograph(gsize):
        for _ in range(int(360 / gsize)):
            color = random_color()
            t.color(color)
            t.circle(100)
            t.setheading(t.heading() + gsize)
            # time.sleep(.5) 
        
def main():
    gapsize = random.randint(5, 10)
    draw_spirograph(gapsize)
    # screen.mainloop() 
    
if __name__ == '__main__':
    t = Turtle()
    t.speed("fast")
    screen = Screen()
    screen.title('Object-oriented spirograph demo')
    screen.bgcolor("grey")
    screen.colormode(255)
    screen.setup(width=800, height=600)
    main()
    screen.exitonclick()    