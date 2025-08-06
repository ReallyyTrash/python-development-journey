import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_car:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    # Successful crossing
    if player.finish_line():
        player.restart()
        car_manager.level_up()
        scoreboard.point()

screen.exitonclick()