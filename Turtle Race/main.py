import turtle
import random
turtle.colormode(255)

my_screen = turtle.Screen()
my_screen.setup(1000, 500)
my_screen.bgcolor("#212121")


def turtle_race():
    
    user_input = (my_screen.textinput("make your bet", "Choose a color(blue, green, yellow, red, orange, indigo, violet):")).lower()
    race_is_on = True
    color_index = 0
    turtle_index = -150
    colors = ["blue", "green", "yellow", "red", "orange", "indigo", "violet"]

    # TURTLE LIST
    turtles = []
    for i in range(7):
        new_turtle = turtle.Turtle()
        turtles.append(new_turtle)

    # TURTLE RACE
    for i in turtles:
        i.shape("turtle")
        i.penup()
        i.color(colors[color_index])
        i.setposition(-480, turtle_index)
        color_index += 1
        turtle_index += 50

    # WIN OR LOSE
    while race_is_on:
        for i in turtles:
            i.forward(random.randint(0, 20))
            if i.xcor() >= 460:
                race_is_on = False
                if (i.color())[0] == user_input:
                    print("You Win")
                else: 
                    print(f"{(i.color())[0]} Won, You Lost")



def turle_race_lines():
    line = turtle.Turtle()
    line.hideturtle()
    line.color("white")
    line.pensize(2)
    line.speed("fastest")

    line.teleport(460, 200)
    line.setposition(460, -200)
    line.teleport(-480, 200)
    line.setposition(-480, -200)
    line.teleport(-480, -200)
    line.setposition(460, -200)
    line.teleport(460, 200)
    line.setposition(-480, 200)

turle_race_lines()
turtle_race()

my_screen.listen()
my_screen.exitonclick()