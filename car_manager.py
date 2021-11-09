from turtle import Turtle
from random import randint, choice


COLORS = ["red", "magenta", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self, scr):
        self.score = 0
        self.scr = scr
        self.cars = [Car(self.scr, self.score)]
        self.car_born_countdown = 0

    def some_car_run(self, score):
        if self.car_born_countdown == 0:
            for car in self.cars:
                if car.step_size == 0:
                    car.run()
                    self.car_born_countdown = randint(1, 20)
                    return
            self.cars.append(Car(self.scr, score))
            self.car_born_countdown = randint(1, 20)
        self.car_born_countdown -= 1

    def all_cars_move(self, player):
        for car in self.cars:
            car.make_step(self.cars)
            if car.ycor() == player.ycor() and -30 <= car.xcor() - player.xcor() <= 30:
                print(f"{player.pos()}   {car.pos()}")
                return False
        self.scr.update()
        return True

    def all_cars_speed_up(self, score):
        for car in self.cars:
            car.score = score
            car.step_size += int(0.5 * car.score * MOVE_INCREMENT)


class Car(Turtle):

    def __init__(self, scr, score):
        super().__init__()
        self.penup()
        self.scr = scr
        self.score = score
        self.shape('square')
        self.shapesize(1, 2)
        self.setheading(180)
        self.standby()
        self.step_size = 0

    # set car speed
    def run(self):
        self.step_size = randint(STARTING_MOVE_DISTANCE + int(0.5 * self.score * MOVE_INCREMENT),
                                 STARTING_MOVE_DISTANCE + self.score * MOVE_INCREMENT)

    # move car to starting position and randomize color:
    def standby(self):
        self.lane = randint(3, int(self.scr.window_height() / 30) - 1)
        self.setx(int(self.scr.window_width() / 2) + 20)
        self.sety(self.lane * 30 - int(self.scr.window_height() / 2) - 20)
        self.color(choice(COLORS))
        self.step_size = 0

    def make_step(self, cars):
        for car in cars:
            if self.lane == car.lane and 0 < self.xcor() - car.xcor() < 100 and self != car:
                print(f"{self.lane} {car.lane}")
                self.step_size = car.step_size
                self.setx(car.xcor() + 100)
        self.forward(self.step_size)
        if self.xcor() < -self.scr.window_width() / 2:
            self.standby()