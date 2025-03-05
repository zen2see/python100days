# DAY23 turtlecross.py
import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player

def setup_screen():
    screen = Screen()
    screen.title('Turtle crossing')
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=800, height=700)
    screen.tracer(0)
    return screen

def flash_player(player):
    screen = Screen()
    player.color("yellow")
    screen.update()
    time.sleep(0.1)
    player.color("blue")

"""
def restart_game():
    player.goto(-385, 0)
    paddle2.goto(380, 0)
    ball.reset_position()
    scoreboard.reset()
screen.onkey(restart_game, "r")
"""


def main(): 
    screen = setup_screen()  
    player = Player()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(player.move_up, "w")
    screen.onkey(player.move_down, "s")    
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_left, "a")
    screen.onkey(player.move_right, "d")    
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")

    game_on = True
    while game_on == True:
        player
        screen.update()
        time.sleep(0.08)
        # player.move()

        # Detect collision with top and bottom walls
        if player.ycor() > 330:
            print("You made it")
            screen.exitonclick()
        """    
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
        """
        
    #if game_on == False:
    #    time.sleep(2)
    #    scoreboard.game_over()
    # screen.mainloop() 
  
if __name__ == '__main__':
    main()