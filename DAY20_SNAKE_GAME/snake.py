import time
from turtle import Turtle, Screen
from snakesegment import Snakesegment
import random
from food import Food
from scoreboard import Scoreboard

"""
Pointer: ((15,0),(0,25),(-15,0),(0,3))
Noel Star: ((0,20),(-5,5),(-20,0),(-5,-5),(0,-20),(5,-5),(20,0),(5,5))
X: ((15,15),(-15,-15),(0,0),(15,-15),(-15,15),(0,0))
Cross: ((-7.5,-15),(7.5,-15),(7.5,-7.5),(15,-7.5),(15,7.5),(7.5,7.5),(7.5,15),(-7.5,15),(-7.5,7.5),(-15,7.5),(-15,-7.5),(-7.5,-7.5))
Right Triangle: ((20,0),(0,-20),(0,0))
Arrow: ((-15,7.5),(-10,0),(-15,-7.5),(5,-7.5),(15,0),(5,7.5))
Parallelogram: ((-30,20),(-40,-20),(30,-20),(40,20)) 
Rhombus: ((0,-20),(-10,0),(0,20),(10,0))
Trapezoid: ((-20,20),(20,20),(30,0),(-30,0))
Pentagon: ((-5,10),(-10,0),(-5,-10),(5,-10),(10,0),(5,10))
Hexagon: ((-10,20),(-20,0),(-10,-20),(10,-20),(20,0),(10,20))
Octagon: ((-10,20),(10,20),(20,10),(20,-10),(10,-20),(-10,-20),(-20,-10),(-20,10))
"""

# Using Turtle.distance
def checkdist(scoreboard, snake, food):
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.goto(random.randint(-280, 260), random.randint(-280, 260))
        # snake.add_segment((Snakesegment.xcor, Snakesegment.ycor))
        snake.add_segment(snake.segments[-1].position())      
        

def setup_screen():
    screen = Screen()
    screen.title('Snake Game')
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=600, height=600)
    screen.tracer(0)
    return screen

def main():
    t = Turtle(shape="square")
    t.shapesize(1,1)
    snake = Snakesegment()
    screen = setup_screen()
    scoreboard = Scoreboard()
    """
    register_shape() function. The first argument is what you will name the shape; 'rectangle',
    in this case. The second argument is the coordinates, so save them as a variable.
    """
    # t = turtle.Turtle()
    # s = turtle.Screen()
    # rectCors = ((-20,10),(20,10),(20,-10),(-20,-10))
    # s.register_shape('rectangle',rectCors);
    # t = Turtle(shape='rectangle')
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Hide the turtle
    # t.hideturtle()
    snake.hideturtle()
    
    # Add Food
    food = Food()

    # Add Scoreboard
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        checkdist(scoreboard, snake, food)

    if game_on == False:
        scoreboard.game_over()

    screen.exitonclick()   
    screen.mainloop() 

if __name__ == '__main__':
    main()