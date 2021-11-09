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
        self.penup()
        self.shape('turtle')
        self.color('brown')
        self.draw_lanes()
        self.setheading(90)
        self.pencolor('black')
        self.start()

    def step_forward(self):
        self.lane += 1
        self.forward(30)

    def step_backward(self):
        if self.lane >= 0:
            self.lane -= 1
            self.backward(30)

    def start(self):
        self.sety(self.lanes[0] - 33)
        self.lane = -1

    def draw_lanes(self):
        self.setheading(0)
        for lane in self.lanes:
            self.setx(-int(self.scr.window_width() / 2))
            self.sety(self.lanes[lane] - 15)
            self.pencolor('white')
            self.pensize(3)
            while self.xcor() <= self.scr.window_width() / 2:
                self.pendown()
                self.forward(30)
                self.penup()
                self.forward(30)
        self.setx(0)