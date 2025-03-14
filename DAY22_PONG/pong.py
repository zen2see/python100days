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

def flash_paddle(paddle):
    screen = Screen()
    paddle.color("yellow")
    screen.update()
    time.sleep(0.1)
    paddle.color("blue")

"""
def restart_game():
    paddle1.goto(-385, 0)
    paddle2.goto(380, 0)
    ball.reset_position()
    scoreboard.reset()
screen.onkey(restart_game, "r")

"""


def main(): 
    screen = setup_screen()  
    paddle1 = Paddle((-385,0))
    paddle2 = Paddle((380, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    
    screen.listen()
    screen.onkey(paddle1.move_up, "w")
    screen.onkey(paddle1.move_down, "s")    
    screen.onkey(paddle2.move_up, "Up")
    screen.onkey(paddle2.move_down, "Down")

    game_on = True
    while game_on == True:
        screen.update()
        time.sleep(0.08)
        ball.move()

        # Detect collision with top and bottom walls
        if ball.ycor() > 330 or ball.ycor() < -330:
            ball.bounce_y()

        if ball.distance(paddle1) < 75 and ball.xcor() < -350:
            print(f"Collision with Paddle1 at: ({ball.xcor()}, {ball.ycor()})")
            flash_paddle(paddle1)
            ball.increase_speed()
            ball.bounce_x()

        elif ball.distance(paddle2) < 75 and ball.xcor() > 350:
            print(f"Collision with Paddle2 at: ({ball.xcor()}, {ball.ycor()})")
            flash_paddle(paddle2)
            ball.increase_speed()
            ball.bounce_x()
        
        # Detect when paddle misses the ball
        if ball.xcor() > 395:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -395:
            ball.reset_position()
            scoreboard.r_point()
    
    if game_on == False:
        time.sleep(2)
        scoreboard.game_over()
    screen.exitonclick() 
    # screen.mainloop() 
  
if __name__ == '__main__':
    main()