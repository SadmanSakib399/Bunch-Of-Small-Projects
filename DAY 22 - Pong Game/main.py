# IMPORTS 
from turtle import Screen, colormode
from classes import Bat, Ground, ScoreBoard, Ball
import time


# SCREEN SETTINGS
colormode(255)
screen = Screen()
screen.setup(width=1500, height=1000)
screen.bgcolor("#212121")
screen.title("Pong game")
screen.tracer(0)


# VARIABLES
time_ = 0.02
game_is_on = True
game_is_pause = True


# FUNCTIONS
def game_pause():
    global game_is_pause
    if not game_is_pause:
        game_is_pause = True
        game_over.game_pause()
    else:
        game_is_pause = False
        game_over.clear()

def bat_1_up():
    if not game_is_pause: 
        bat_1.up()
def bat_1_down():
    if not game_is_pause:  
        bat_1.down()
def bat_2_up():
    if not game_is_pause:  
        bat_2.up()
def bat_2_down():
    if not game_is_pause:  
        bat_2.down()

        

# OBJECTS
ball = Ball()
bat_1 = Bat((-730, 0), "RED")
bat_2 = Bat((730, 0), "BLUE")
ground = Ground()
score_1 = ScoreBoard((-80, 430))
score_2 = ScoreBoard((80, 430))
game_over = ScoreBoard((0, 0))


# KEYBIND
screen.listen()
screen.onkey(game_pause, key="space")
screen.onkey(game_pause, key="Return")

screen.onkeypress(bat_1_up, key="w")
screen.onkeypress(bat_1_up, key="W")
screen.onkeypress(bat_1_down, key="s")
screen.onkeypress(bat_1_down, key="S")

screen.onkeypress(bat_2_up, key="Up")
screen.onkeypress(bat_2_down, key="Down")


# FUNCTION CALL
ball.starting()
score_1.score_write()
score_2.score_write()


# MAIN GAMELOOP
while game_is_on:

    screen.update()
    time.sleep(time_)

    # MOVING THE BALL
    if not game_is_pause:
        ball.move()

    # CHECK COLLISION 
    if ball.xcor() >= 720 or ball.xcor() <= -720:
        if ball.distance(bat_1) <= 50 or ball.distance(bat_2) <= 50:
            ball.change_angle()
            if time_ > 0.008:
                time_ += -0.001
            

    # INCREASE SCORE
    if ball.xcor() >= 780 or ball.xcor() <= -780:
        if ball.xcor() >= 780:
            score_1.score += 1
            score_1.score_write()
        if ball.xcor() <= -780:
            score_2.score += 1
            score_2.score_write()
        game_is_pause = True
        ball.starting()
        bat_1.starting((-730, 0))
        bat_2.starting((730, 0))

    #WALL COLLISON
    if ball.ycor() >= 480 or ball.ycor() <= -480:
        ball.bounce()

    # GAME OVER 
    if score_1.score == 5 or score_2.score == 5:
        screen.clear()
        screen.bgcolor("#212121")
        game_over.gameover( color= "BLUE" if score_1.score == 5 else "RED")
        game_over.won(color= "BLUE" if score_1.score == 5 else "RED")
        game_is_on = False

screen.exitonclick()









