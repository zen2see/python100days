from os import system, name
import time
from turtle import Turtle, Screen

# docs.python.org/3.3/library/turtle.html
# docs.python.org/3/library/tkinter.html
# You’ll need  Tk interface package installed  
# Running python -m tkinter should demonstrating a simple Tk interface
# tcl.tk/man/tcl8.4/TkCmd/colors.htm
# cs111.wellesley.edu/labs/lab01/colors

# NOTES
# home() = center of screen
# pos() = x-y coordinates
# clearscreen()
# fillcolor('green')
# abs(pos()) < 1 is a good way to know when the turtle is back at its home position.

t = Turtle()
t.shape("turtle")
t.color("green")
screen = Screen()
screen.title('Object-oriented turtle demo')
screen.bgcolor("orange")
screen.setup(width=600, height=600)

def main():
    for _ in range(4):
        t.forward(100)
        t.right(90)
    screen.mainloop()
    
if __name__ == '__main__':
    main()