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
    screen = setup_screen()
    scoreboard = Scoreboard()
    snake = Snakesegment(scoreboard)
    food = Food()
    game_on = True
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
    
    # Add Scoreboard
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        checkdist(scoreboard, snake, food)
    
    if game_on == False:
        time.sleep(2)
        scoreboard.game_over()
        screen.exitonclick() 
    screen.mainloop() 

if __name__ == '__main__':
    main()

    """
    Levels and Speed: Increase the game's difficulty as the player's score increases by 
    speeding up the snake's movement or adding obstacles.
    # Add this before the loop
    speed = 0.1
    # Inside the loop
    while game_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    checkdist(scoreboard, snake, food)
    
    # Increase speed as score increases
    if scoreboard.score % 5 == 0:  # Increase speed every 5 points
        speed *= 0.9  # Adjust the factor as needed
    
    Scoreboard Enhancements: Display the top scores or track scores over multiple sessions.
    # Add to __init__ method
    self.high_scores = []

    def display_high_scores(self):
        self.clear()
        self.goto(0, 0)
        self.write("High Scores:", align=ALIGNMENT, font=FONT)
        for index, score in enumerate(self.high_scores[:5]):
            self.goto(0, -30 * (index + 1))  # Adjust position for each score
            self.write(f"{index + 1}. {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.high_scores.append(self.score)
        self.high_scores.sort(reverse=True)
        self.display_high_scores()
        sys.exit()
    Custom Shapes: Use the custom shapes you've defined for the snake or food.
    # Register shapes at the beginning of main()
    screen.register_shape('rectangle', ((-20,10),(20,10),(20,-10),(-20,-10)))
    # Add more shapes as needed...

    # Use the shapes
    snake.shape('rectangle')
    
    Sound Effects: Add sound effects for when the snake eats the food, when the game starts, 
    or when the game ends.
    from playsound import playsound

    def checkdist(scoreboard, snake, food):
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.goto(random.randint(-280, 260), random.randint(-280, 260))
            snake.add_segment(snake.segments[-1].position())
            playsound('eat_sound.mp3')  # Add the path to your sound file
    5. Themes
        Themes: Add different themes for the game (e.g., jungle, desert, underwater)
        and change the snake and food appearances accordingly.
        If you need help implementing any of these features, just let me know! Happy coding! 🐍🎮
        themes = {
            "jungle": {"bg": "green", "snake_color": "brown", "food_color": "red"},
            "desert": {"bg": "yellow", "snake_color": "orange", "food_color": "blue"},
            # Add more themes...
        }

        # Apply a theme
        selected_theme = themes["jungle"]  # Choose a theme
        screen.bgcolor(selected_theme["bg"])
        snake.color(selected_theme["snake_color"])
        food.color(selected_theme["food_color"])
    """