import turtle
import pandas
from classes import ScoreBoard

BACKGROUND_IMG = "100 Days Of Learning Python/DAY 25 - U.S. States Guessing Game/states_img.gif"
data = pandas.read_csv("100 Days Of Learning Python/DAY 25 - U.S. States Guessing Game/50_states.csv")
Game_is_on = True

my_screen = turtle.Screen()
my_screen.title("GUESS THE STATES")
my_screen.addshape(BACKGROUND_IMG)

score_board = ScoreBoard()
guessed_states = []

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

turtle.shape(BACKGROUND_IMG)
states_list = data["state"].to_list()

# MAIN_GAME_LOOP
while Game_is_on:

    user_guess = (my_screen.textinput(f"{score_board.score} / 50 is Correct.", "Guess the states names:")).title()
    if user_guess in states_list and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        positon = data[data["state"] == user_guess]
        pen.goto(int(positon.x), int(positon.y))
        pen.write(user_guess, font = ("Arial", 12, "bold"))
        score_board.score += 1
    
    if score_board.score == 50:
        Game_is_on = False

    if user_guess == "Exit":
        for i in guessed_states:
            states_list.remove(i)
        Game_is_on = False
        pandas.DataFrame(states_list).to_csv("F:/python/pythonProject/projects OOP/US Guessing Game/remaining_states.csv")

my_screen.exitonclick()