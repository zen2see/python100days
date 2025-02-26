# DAY22 pong.py
import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

def setup_screen():
    screen = Screen()
    screen.title('Pong Game')
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=800, height=700)
    screen.tracer(0)
    return screen

def main():   
    paddle1 = Paddle()
    ball = Ball()
    screen = setup_screen()
    scoreboard = Scoreboard()
    game_on = True

    screen.listen()    
    screen.onkey(paddle1.up, "Up")
    screen.onkey(paddle1.down, "Down")
    screen.onkey(paddle1.left, "Left")
    screen.onkey(paddle1.right, "Right")

    while game_on:
        screen.update()
        time.sleep(0.1)
        # ball.move()
        # checkdist(scoreboard, snake, food)
    
    if game_on == False:
        time.sleep(2)
        scoreboard.game_over()
        screen.exitonclick() 
    screen.mainloop() 

if __name__ == '__main__':
    main()