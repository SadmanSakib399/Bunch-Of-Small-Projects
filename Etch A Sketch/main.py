import turtle
import random
tam = turtle.Turtle()
my_screen = turtle.Screen()
turtle.colormode(255)

pen_down_custom = True
eraser = False


# PAN MOVEMENT
def forward():
    tam.forward(10)
def backward():
    tam.backward(10)
def left():
    tam.left(15)
def right():
    tam.right(15)


# PAN CUSTOMIZE 
def pen_up_down():
    global pen_down_custom
    if pen_down_custom:
        pen_down_custom = False
        tam.penup()
    else:
        pen_down_custom = True
        tam.pendown()

def colorchange():
    tam.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def pen_size1():
    tam.pensize(1)   
def pen_size2():
    tam.pensize(3)  
def pen_size3():
    tam.pensize(5)

def erase():
    global eraser
    if not eraser:
        eraser = True
        tam.pencolor("white")
    else:
        eraser = False
        tam.pencolor("black")        


# RESET
def clear():
    tam.clear() 
    tam.teleport(0,0)


# KEY
my_screen.onkeypress(forward, key='w',)
my_screen.onkeypress(backward, key='s')
my_screen.onkeypress(left, key='a')
my_screen.onkeypress(right, key='d')

my_screen.onkey(pen_up_down, key='q',)
my_screen.onkey(colorchange, key='e',)
my_screen.onkey(erase, key='space',)
my_screen.onkey(clear, key='c',)

my_screen.onkey(pen_size1, key='1',)
my_screen.onkey(pen_size2, key='2',)
my_screen.onkey(pen_size3, key='3',)


my_screen.listen()
my_screen.exitonclick()