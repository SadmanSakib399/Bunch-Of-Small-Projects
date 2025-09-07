from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(100,300)
        self.score = 0
    
    def write_score(self):
        self.clear()
        self.write(f"{self.score} / 50", font=("Arial", 40, "bold"))