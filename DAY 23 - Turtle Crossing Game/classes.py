from turtle import Turtle
import random


class MainTurtle(Turtle):

    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.setheading(90)
        self.new_lvl_start()
        self.penup()
    
    def Up(self):
        self.forward(20)

    def new_lvl_start(self):
        self.teleport(0, -460)

    
class Car(Turtle):

    def __init__(self, shape = "square", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(1, 2)
        self.setheading(180)
        self.penup()
        self.color_list = [ "#FF5733", "#33FF57", "#C70039", "#9C27B0", "#E91E63", "#00BCD4", "#FF9800",  "#4CAF50", "#8BC34A", "#3F51B5", "#F44336", "#FFEB3B", "#CDDC39",]
        self.color(random.choice(self.color_list))
        self.teleport((500 + (random.randint(10, 1000))),(random.randint(-390, 390)))

    def position(self):
        self.teleport( 500,(random.randint(-390, 390)))

    def move(self):
        self.forward(20)


class BackGroung(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("#919191")
        self.pensize(3)
        self.speed("fastest")
        self.teleport(-500, -400)
        self.goto(500, -400)
        self.teleport(-500, 400)
        self.goto(500, 400)
        

class ScoreBoard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.level = 1
        self.color("white")
        self.teleport(-400, 420)
        self.score_write()

    def score_write(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=("Arial", 40, "bold"))

    def game_over(self):
        self.teleport(0,0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 80, "bold"))