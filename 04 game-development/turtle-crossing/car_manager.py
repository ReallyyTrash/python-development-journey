from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_car =[]
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1,6)
        if chance ==1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.up()
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += self.carspeed*0.5
