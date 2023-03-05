from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def update_score(self):

        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score += 1
        self.write(f"Current Score : {self.score} ")
