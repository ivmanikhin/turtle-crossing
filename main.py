from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
score = 0
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('grey')
screen.tracer(0)
scoreboard = Scoreboard(screen, score)
car_man = CarManager(screen)
player = Player(screen, car_man.lanes)
game_is_on = True
screen.listen()
screen.onkey(fun=player.step_forward, key="Up")
screen.onkey(fun=player.step_backward, key="Down")

while game_is_on:
    sleep(0.025)
    car_man.some_car_run(score)
    game_is_on = car_man.all_cars_move(player)
    if player.lane > len(car_man.lanes):
        player.start()
        score += 1
        scoreboard.update(score)
        car_man.all_cars_speed_up(score)

screen.exitonclick()
