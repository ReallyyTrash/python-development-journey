FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level = {self.level}", align= "center", font= FONT)

    def point(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, "Center", FONT )
