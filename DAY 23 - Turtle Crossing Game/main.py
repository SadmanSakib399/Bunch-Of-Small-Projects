# IMPORTS
import time
from turtle import Screen
from classes import MainTurtle, Car, BackGroung, ScoreBoard

# SCREEN SETTINGS
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("#212121")
screen.tracer(0)

# VARIABLES
game_speed = 0.1
car_amount = 20
game_is_on = True

# CLASSES
turtle = MainTurtle()
background = BackGroung()
score = ScoreBoard()

# KEYS
screen.listen()
screen.onkeypress(turtle.Up, key="W")
screen.onkeypress(turtle.Up, key="w")

# MAIN GAME LOOP
# genaration of cars
cars = []
for i in range(car_amount):
    i = Car()
    cars.append(i)

# game loop
while game_is_on:
    time.sleep(game_speed)
    screen.update()

    for i in cars:
        i.move()

    for i in cars:

        if i.xcor() <= -500:
            i.position()

        if i.distance(turtle) <= 20:
            score.game_over()
            game_is_on = False

    if turtle.ycor() >= 420:
        score.level += 1
        game_speed -= 0.005
        for i in range(5):
            i = Car()
            cars.append(i)
        score.score_write()
        turtle.new_lvl_start()

screen.exitonclick()