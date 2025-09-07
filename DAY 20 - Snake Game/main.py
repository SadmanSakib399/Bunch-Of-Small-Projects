# IMPORTS
import time 
from turtle import Screen, colormode
from Snake  import Snake
from food   import Food
from score  import ScoreBoard
from level  import Lvl

# CONSTANT VARIABLES 
BACKGROUND_COLOR = "#212121"
SCREEN_TITLE = "My snake game"
GAME_SPEED = 0.1

# SCREEN SETTINGS
colormode(255)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# VARIABLES
game_is_on = True
game_pause = False

# OBJECTS
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score_paused = ScoreBoard()
lvl = Lvl()

# FUNCTIONS
def pause():
    global game_pause
    if not game_pause:
        game_pause = True
        score_paused.clear()
    else:
        game_pause = False
        score_paused.game_pause()

# KEYS 
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")
screen.onkey(pause, key="space")

# MAIN GAME LOOP
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)
    if game_pause:
        snake.move()
    scoreboard.scores()

    # PLAYING
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_inc()
        snake.grow()

    #GAME OVER (WALL)
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or  snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        scoreboard.reset()
        for i in snake.snake[3:]:
            snake.snake.remove(i)
            i.hideturtle()
        snake.starting_position()

    # GAME OVER (TAIL)
    for i in snake.snake[1:]:
            if i.distance(snake.head) <= 10:
                scoreboard.reset()
                for i in snake.snake[3:]:
                    snake.snake.remove(i)
                    i.hideturtle()
                snake.starting_position()

screen.exitonclick()
