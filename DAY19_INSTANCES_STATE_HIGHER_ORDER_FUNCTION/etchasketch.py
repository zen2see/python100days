from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.title('Object-oriented Etch-A-Sketch demo')
screen.bgcolor('grey')
screen.colormode(255)
screen.setup(width=800, height=600)

# Movement functions
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)
def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)
# CLear
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def main():
    screen.listen()
    screen.onkey(move_forward, 'w')
    screen.onkey(move_backward, 's')
    screen.onkey(turn_left, 'a')
    screen.onkey(turn_right, 'd')
    screen.onkey(clear, 'x')


    # screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()