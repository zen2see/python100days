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
    screen = setup_screen()  
    paddle1 = Paddle((-385,0))
    paddle2 = Paddle((380, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    # Cooldown to prevent multiple collisions in a short time
    collision_cooldown = False

    def reset_cooldown():
        nonlocal collision_cooldown
        collision_cooldown = False
    
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

        # Detect collision with paddles
        # if (ball.distance(paddle1) < 40) or (ball.distance(paddle2) < 40):
        #    print(ball.xcor(), ball.ycor())
        #    if paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50:
        #         offset = ball.ycor() - paddle1.ycor()  # Distance from paddle center
        #         ball.y_move = offset / 10  # Adjust bounce angle
        #         ball.bounce_x()
        if ball.distance(paddle1) < 40:
            print(f"Collision with Paddle1 at: ({ball.xcor()}, {ball.ycor()})")
            if paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50:
                offset = ball.ycor() - paddle1.ycor()  # Distance from paddle center
                ball.y_move += offset / 10  # Adjust bounce angle
                ball.bounce_x()
                collision_cooldown = True
                screen.ontimer(reset_cooldown, 50)  # Reset cooldown after 50ms

        elif ball.distance(paddle2) < 40:
            print(f"Collision with Paddle2 at: ({ball.xcor()}, {ball.ycor()})")
            if paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50:
                offset = ball.ycor() - paddle2.ycor()  # Distance from paddle center
                ball.y_move += offset / 10  # Adjust bounce angle
                ball.bounce_x()
                collision_cooldown = True
                screen.ontimer(reset_cooldown, 50)  # Reset cooldown after 50ms
           
        #BOUNDING BOX METHOD
        # Check for collision with paddle1
        #if -370 < ball.xcor() < -360 and paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50:
        #    ball.bounce_x()
        # Check for collision with paddle2
        #if 360 < ball.xcor() < 370 and paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50:
        #    ball.bounce_x()
        
        # Detect when paddle misses the ball
        if ball.xcor() > 395:
            ball.reset_position()
            scoreboard.l_point()

        if ball.xcor() < -395:
            ball.reset_position()
            scoreboard.r_point()
    
    # if game_on == False:
    #     time.sleep(2)
    #     scoreboard.game_over()
    screen.exitonclick() 
    # screen.mainloop() 
  
if __name__ == '__main__':
    main()