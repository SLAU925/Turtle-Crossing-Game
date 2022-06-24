from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        n = random.randint(1,6)
        if(n == 1):
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(320, random.randint(-250,250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)
    
    def faster(self):
        self.speed += MOVE_INCREMENT