from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, scr, lanes):
        super().__init__()
        self.lanes = lanes
        self.lane = -1
        self.scr = scr
        self.shape('turtle')
        self.pencolor('black')
        self.color('brown')
        self.penup()
        self.setheading(90)
        self.start()

    def step_forward(self):
        self.lane += 1
        self.forward(30)

    def step_backward(self):
        if self.lane >= 0:
            self.lane -= 1
            self.backward(30)

    def start(self):
        self.sety(self.lanes[0] - 30)
        self.lane = -1
