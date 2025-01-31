class Car:
    """ TEST CAR BLUEPRINT """
    def __init__(self, num_of_seats, speed):
        self.num_of_seats = num_of_seats
        self.speed = speed
    
    def drive(self):
        print("IN DRIVE")
        self.speed += 10

    def brake(self):
        print("BRAKE")
        self.speed -= 10

mycar = Car(num_of_seats=4, speed=100)
mycar.drive()
print(mycar.speed)