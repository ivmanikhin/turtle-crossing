from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, scr, score):
        super().__init__()
        self.scr = scr
        self.hideturtle()
        self.penup()
        self.goto(-self.scr.window_width() / 2 + 30, self.scr.window_height() / 2 - 40)
        self.update(score)

    def update(self, score):
        self.clear()
        self.write(f"Level {score + 1}", False, 'left', FONT)
