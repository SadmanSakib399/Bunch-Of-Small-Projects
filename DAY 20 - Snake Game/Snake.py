import turtle

MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.snake = []
        self.starting_snake()
        self.head = self.snake[0]

    def starting_snake(self):
        snake_position = 0
        for i in range(3):
            i = turtle.Turtle("square")
            i.color("white")
            i.penup()
            i.teleport(0 + snake_position, 0)
            snake_position -= 20
            self.snake.append(i)
    
    def starting_position(self):
        self.snake[0].goto(0, 0)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            pos = self.snake[i - 1].position()
            self.snake[i].goto(pos)
        self.head.forward(MOVE_DISTANCE)

    def grow(self,):
        pos = self.snake[-1].position()
        i = turtle.Turtle("square")
        i.color("white")
        i.penup()
        i.teleport(pos[0] + 20, pos[1])
        self.snake.append(i)
        

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
