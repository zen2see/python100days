from os import system, name
import time, random
from turtle import Turtle, Screen
import colorgram

# docs.python.org/3.3/library/turtle.html
# docs.python.org/3/library/tkinter.html
# You’ll need  Tk interface package installed  
# Running python -m tkinter should demonstrating a simple Tk interface
# tcl.tk/man/tcl8.4/TkCmd/colors.htm
# cs111.wellesley.edu/labs/lab01/colors
# tinket.io/docs/colors
# Colorgram - https://pypi.org/project/colorgram.py/ pip3 install colorgram.py


# RANDOM COLOUR USING RGB
def extract_colors(image_path, num_colors):
    # Extract 6 colors from an image.
    colors = colorgram.extract(image_path, num_colors)
    return colorgram.extract(image_path, num_colors)  
    
def main():
    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    """
    A color extracted from an image. Its properties are:
    Color.rgb - The color as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210).
    Color.hsl - The color as a namedtuple of HSL from 0 to 255, e.g. (h=230, s=255, l=203).
    Color.proportion - The proportion of the image that is in the extracted color from 0 to 1.
    """
    new_colors = []
    colors = extract_colors('MoldOnYarn.png', 100)

    t = Turtle()
    # t.shape("turtle")
    screen = Screen()
    screen.title('Object-oriented Hurst Painting demo')
    screen.bgcolor("grey")
    screen.colormode(255)
    screen.setup(width=800, height=600)
    num_dots = 100

    for index, color in enumerate(colors):
        rgb = color.rgb # e.g. (255, 151, 210)
        hsl = color.hsl # e.g. (230, 255, 203)
         # Accessing RGB values
        red, green, blue = rgb.r, rgb.g, rgb.b
        # Accessing HSL values
        hue, saturation, lightness = hsl.h, hsl.s, hsl.l
        # Accessing proportions e.g. 0.34 
        proportion = color.proportion  
        # RGB and HSL are named tuples, so values can be accessed as properties.
        # These all work just as well:
        the_colors = (red, green, blue)
        new_colors.append(the_colors)
        t.penup()
        t.hideturtle()
        """
        red = rgb[0] = rgb.r
        blue = rgb.b
        green = rgb.g
        hue = hsl.h = hsl[0]
        saturation = hsl.s = hsl[1] 
        lightness = hsl.l = hsl[2]
        """
        # print(index)
        # print(proportion, red, green, blue, hue, saturation, lightness)
        # print(new_colors)
        """
        """
        
    for dots in range(1, num_dots+1):
        t.dot(20, random.choice(new_colors))
        t.forward(20)

        if dots % 10 == 0:
            t.setheading(90)
            t.forward(20)
            t.setheading(180)
            t.forward(200)
            t.setheading(0)

    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()