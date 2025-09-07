from turtle import Turtle
import random

class Bat(Turtle):

    def __init__(self, position, color,):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(1, 5)
        self.color(color)
        self.goto(position)

    def starting(self, position):
        self.goto(position)

    def up(self):
        if self.ycor() < 450:
            self.forward(20)

    def down(self):
        if self.ycor() > -450:
            self.backward(20)



class Ground(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.hideturtle()
        self.speed("fastest")
        self.dotted_line()

    def dotted_line(self):
        self.teleport(0, 470)
        self.setheading(270)
        for _ in range(14):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(50)



class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)

    def score_write(self):
        self.clear()
        self.write(self.score, False, align="center", font=("Arial", 40, "bold"))
    
    def gameover(self, color):
        self.color(color)
        self.write("GAME OVER", False, align="center", font=("Arial", 80, "bold"))
    
    def won(self, color):
        self.teleport(0, -40)
        self.color(color)
        self.write(f"{color} WON", False, align="center", font=("Arial", 40, "bold"))
    
    def game_pause(self):
        self.write("PAUSED", False, align="center", font=("Arial", 80, "bold"))
    


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.angles = [-15 , -10, -5, 0, 5, 10, 15]


    def starting(self):
        self.teleport(0, 0)    
        if random.randint(1, 2) == 1:
            self.setheading(180)
        else: 
            self.setheading(0)

    def change_angle(self):
            self.left(180 + random.choice(self.angles))

    def move(self):
        self.forward(10)

    def bounce(self):
        if 0 <= self.heading() < 90:
            self.setheading(180 - self.heading())  
        elif 90 <= self.heading() < 180:
            self.setheading(180 + (180 - self.heading()))  
        elif 180 <= self.heading() < 270:
            self.setheading(360 - (self.heading() - 180))
        elif 270 <= self.heading() < 360:
            self.setheading(360 - self.heading())