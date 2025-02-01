import anothermodule 
# import turtle - timmy = turtle.Turtle()
# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen 
# PYTHON PACKAGES https://pypi.org/
import prettytable

timmy = Turtle()
print(timmy)
#print(anothermodule.another_variable)
# print(my_screen.canvheight, my_screen.canvwidth)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(10)
my_screen = Screen()
my_screen.exitonclick()
