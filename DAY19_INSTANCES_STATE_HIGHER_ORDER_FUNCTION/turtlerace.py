from turtle import Turtle, Screen
import random

t = Turtle(shape='turtle')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.title('Object-oriented Turtlerace demo')
screen.bgcolor('grey')
screen.colormode(255)
screen.setup(width=500, height=400)

def turtles(tnew):
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
    
def randommove(tnew):
    for turtle in tnew:
        rdist = random.randint(0, 10)
        turtle.goto(x=turtle.xcor() + rdist, y=turtle.ycor())
    return tnew

def race(tnew):
    randommove(tnew)

def main():
    tnew = []
    race_on = False
    turtles(tnew)
    t.hideturtle()
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race> Enter a color: ")
    if user_bet:
        race_on = True
    while race_on:
        race(tnew)
        for turtle in tnew:
            if turtle.xcor() > 225:  # 225 is half of the width of the screen (500/2 - 25 for turtle)
                race_on = False
                winning_color = turtle.pencolor()
                print(f"The winner is the {winning_color} turtle!")
                if winning_color == user_bet:
                    print("You won!")
                else:
                    print("You lost!")
                break 
    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()