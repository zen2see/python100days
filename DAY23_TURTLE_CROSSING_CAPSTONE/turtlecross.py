# DAY23 turtlecross.py
import time
import random
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

def setup_screen():
    screen = Screen()
    screen.title('Turtle crossing')
    screen.bgcolor('black')
    screen.colormode(255)
    screen.setup(width=700, height=700)
    screen.tracer(0)
    return screen

def flash_player(screen, player):
    screen = Screen()
    player.color("yellow")
    screen.update()
    time.sleep(0.1)
    player.color("blue")

def generate_car(cars):
    if random.randint(1, 6) == 1:
        new_car = CarManager()
        collision_detected = any(new_car.is_collision(car) for car in cars)
        # Check if cars are in the same horizontal plane
        same_horizontal_plane_detected = any(abs(new_car.ycor() - car.ycor()) < 20 for car in cars)  
        # Check if cars are in the same vertical plane
        same_vertical_plane_detected = any(abs(new_car.xcor() - car.xcor()) < 20 for car in cars)  
        # Check for collisions
        if not collision_detected and not same_horizontal_plane_detected and not same_vertical_plane_detected:
            cars.append(new_car) 
        else:
            print("Collision or same plane detected during car generation.")
            

def restart_game(screen, player, scoreboard, cars):
    screen.clearscreen()  # Clear the screen
    screen = setup_screen() 
    player = Player()
    player.goto(0, -330)
    scoreboard.reset()
    cars.clear()
    screen.update() 
    setup_key_bindings(screen, player, scoreboard, cars)
    return screen, player, scoreboard, cars

def restart_game_handler(screen, player, scoreboard, cars):
        screen, player, scoreboard, cars = restart_game(screen, player, scoreboard, cars)
        game_loop(screen, player, cars, scoreboard)

def setup_key_bindings(screen, player, scoreboard, cars):
    screen.listen()
    screen.onkey(player.move_up, "w")
    screen.onkey(player.move_down, "s")    
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_left, "a")
    screen.onkey(player.move_right, "d")    
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")
    screen.onkey(lambda: restart_game_handler(screen, player, scoreboard, cars), "r")

def game_loop(screen, player, cars, scoreboard):
    game_on = True
    while game_on:
        screen.update() 
        time.sleep(0.08)
        generate_car(cars)
        for car in cars:
            car.move(cars)
            if car.distance(player) < 20:
                # scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
                print("collision")
                game_on = False
                print("Calling scoreboard.game_over()")
                scoreboard.game_over()
                screen.update() 
                # Exit the funtion after the game over is called
                return
        # Remove cars that are fully off-screen        
        cars = [car for car in cars if car.xcor() >= -400]
        # Detect collision with top and bottom walls
        if player.ycor() > 330:
            print("You made it")
            # Add point
            scoreboard.levelup()
            scoreboard.point()
            screen.update()
            # Reset position after scoring
            player.goto(0, -330)
            # Increase car speed
            for car in cars:
                car.level_up()
            # screen.exitonclick()

def main(): 
    screen = setup_screen()  
    player = Player()
    cars = [] 
    scoreboard = Scoreboard()
    setup_key_bindings(screen, player, scoreboard, cars)
    game_loop(screen, player, cars, scoreboard)
    screen.mainloop()     
    
if __name__ == '__main__':
    main()

"""
USE OF LAMBDA:
import random 
names = ['Mary', 'Isla', 'Sam'] 
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde'] 
for i in range(len(names)):     
	names[i] = random.choice(code_names) 
print names 
# => ['Mr. Blonde', 'Mr. Orange', 'Mr. Blonde'] 

COULD BE REWRITTEN TO SOMETHING LIKE THIS:
import random 
names = ['Mary', 'Isla', 'Sam'] 
secret_names = map(lambda x: random.choice(['Mr. Pink',                                        
'Mr. Orange', 'Mr. Blonde']), names)
"""