from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.title('Object-oriented Listen demo')
screen.bgcolor("grey")
screen.colormode(255)
screen.setup(width=800, height=600)

def move_forward():
    t.forward(10)


def main():
    screen.listen()
    screen.onkey(key="space", fun=move_forward)

    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()