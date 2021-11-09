from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, scr):
        super().__init__()
        self.scr = scr
        self.shape('turtle')
        self.pencolor('black')
        self.color('brown')
        self.penup()
        self.setheading(90)
        self.sety(40 - int(self.scr.window_height() / 2))

    def step_forward(self):
        for i in range(30):
            self.forward(1)

    def step_backward(self):
        if self.ycor() > 40 - int(self.scr.window_height() / 2):
            self.backward(30)

    def start(self):
        self.sety(40 - int(self.scr.window_height() / 2))
