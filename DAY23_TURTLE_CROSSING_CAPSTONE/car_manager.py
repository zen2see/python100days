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
        # slf.goto(300, random.randint(-250, 250))
        # Assign random speed to each car
        # self.move_speed = random.randint(-1,3) + STARTING_MOVE_DISTANCE
        self.speed = random.randint(1, 10) 
    
    def is_collision(self, other_car):
        # return self.distance(other_car) < 6
        distance = self.distance(other_car)
        if distance < 10 and self.speed > other_car.speed:
            return True
        return False
    
    # def move(self, other_cars):
    #     new_x = self.xcor() - self.move_speed
    #     print("new_x ", new_x)
    #     for car in other_cars:
    #         print("self", self.xcor())
    #         print("other_cars", car.xcor())
    #         if self.is_collision(car):
    #             print("Collision with car")
    #         #     return # pause execution by exiting the move method
    #     self.goto(new_x, self.ycor())
    #     print(new_x)

    def move(self, cars):
        new_x = self.xcor() - self.speed
        for car in cars:
            if car != self and self.is_collision(car):
                print("Collision detected, adjusting position.")
                self.speed = car.speed  # Adjust speed to avoid collision
                new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    # def move(self):
    #     self.goto(self.xcor() - self.speed, self.ycor())
    def move(self, cars):
        new_x = self.xcor() - self.speed
        for car in cars:
            if car != self and self.is_collision(car):
                print("Collision detected, adjusting position.")
                self.speed = car.speed  # Adjust speed to avoid collision
                new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())