from turtle import Turtle, Screen

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

def main():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race> Enter a color: ")
    # t.hideturtle()
    # t.goto(x=-230, y=-100)
    turtles()
    # screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()