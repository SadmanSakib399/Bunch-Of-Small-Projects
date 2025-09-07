from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("Data.txt", "r") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
            with open("Data.txt", "w") as data:
                data.write("0")
        self.penup()
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)

    def score_inc(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode="w") as data:
                data.write(f"{str(self.high_score)}")
        self.score = 0
        self.scores

    def game_pause(self):
        self.teleport(0, 0)
        self.write(f"Game Paused", move=False, align='center', font=('Arial', 30, 'normal'))

    def scores(self):
        self.clear()
        self.write(f"score: {self.score}  high score: {self.high_score}", move=False, align='center', font=('Arial', 16, 'normal'))


