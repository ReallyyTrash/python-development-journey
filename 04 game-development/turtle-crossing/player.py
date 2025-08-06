from turtledemo.penrose import start

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle as Tut

class Player(Tut):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def restart(self):
        self.goto(STARTING_POSITION)