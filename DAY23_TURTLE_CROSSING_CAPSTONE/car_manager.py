from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["red", "blue", "green", "yellow", "orange"]))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=random.randint(2,4))
        self.goto(random.randint(400, 405), random.randint(-340, 340))
        # Assign random speed to each car
        # Use a different attribute name to avoid conflict with the speed method - DO Not use self.speed
        self.car_speed = random.randint(1, 10) 
    
    def is_collision(self, other_car):
        # return self.distance(other_car) < 6
        distance = self.distance(other_car)
        if distance < 10 and self.car_speed > other_car.car_speed:
            return True
        return False

    def move(self, cars):
        new_x = self.xcor() - self.car_speed
        for car in cars:
            if car != self and self.is_collision(car):
                print("Collision detected, adjusting position.")
                self.car_speed = car.car_speed  # Adjust speed to avoid collision
                new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        return self.car_speed