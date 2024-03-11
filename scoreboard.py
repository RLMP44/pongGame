from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.report_score()

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1

    def report_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"{self.l_score}  -  {self.r_score}", align="center", font=("Corsiva", 30, "normal"))

