import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkeypress(player.move, "Up")

n = 0

while game_is_on:
    time.sleep(0.03)
    screen.update()
    car_manager.add_car()
    car_manager.move()

    for car in car_manager.cars:
        if(player.distance(car) < 20):
            game_is_on = False
            scoreboard.game_over()

    if(player.ycor() > 280):
        scoreboard.level += 1
        scoreboard.update()
        car_manager.faster()
        player.reset()



screen.exitonclick()
