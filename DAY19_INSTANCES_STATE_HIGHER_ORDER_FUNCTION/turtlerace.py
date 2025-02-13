from turtle import Turtle, Screen
import random

t = Turtle(shape='turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.title('Object-oriented Turtlerace demo')
screen.bgcolor('grey')
screen.colormode(255)
screen.setup(width=500, height=400)

def turtles():
    tnew = []
    for color in colors:
        tnew_turtle = t.clone()
        tnew_turtle.color(color)
        tnew_turtle.penup()
        tnew.append(tnew_turtle) 
    
    y_position = -100
    for turtle in tnew:
        turtle.goto(x=-230, y=y_position)
        y_position += 40
    
    return tnew
    
def randommove():
    rdist = random.randint(0, 10)
    return rdist

def race():
    for turtle in turtles.tnew:
        x_position = randommove()  
        turtle.goto(turtle.x+x_position, y=None)

def main():
    race_on = False
    turtles()
    t.hideturtle()
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race> Enter a color: ")
    if user_bet:
        race_on = True
    while race_on:
        race()
    
    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()