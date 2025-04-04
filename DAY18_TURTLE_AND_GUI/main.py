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

t = Turtle()
t.shape("turtle")
# t.color("green")
screen = Screen()
screen.title('Object-oriented turtle demo')
screen.bgcolor("orange")
screen.setup(width=800, height=600)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SeaGreen"]

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(50)
        t.right(angle)

def main():
    # for _ in range(52):
        ## Square
        # t.forward(100)
        # t.right(90)
        
        ## Dashed line
        # t.forward(10)
        # t.penup()
        # t.forward(10)
        # t.pendown()
     
     ## Triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
     ## Divide by # of sides
    for sides_num in range(3, 11): 
        t.color(random.choice(colors))   
        draw_shape(sides_num)
        # t.penup()
        # t.forward(100) # Move forward to space out shapes
        # t.pendown()
        # time.sleep(1)

    #t.penup()
    #t.setpos(0,20)        
    screen.mainloop() 
    
if __name__ == '__main__':
    main()