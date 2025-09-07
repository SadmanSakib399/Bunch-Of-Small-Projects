from turtle import Turtle

class Lvl(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#919191")
        self.teleport(300, 300)
        self.pensize(10)
        self.goto(300, -300)
        self.goto(-300, -300)
        self.goto(-300, 300)
        self.goto(300, 300)
        self.hideturtle()
        
    