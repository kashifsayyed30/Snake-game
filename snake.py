from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []  # empty list
        self.create_snake()
        self.head = self.snake[0]  # head of the snake. t1 objet

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        tur = Turtle(shape="square")
        tur.penup()
        tur.color("white")
        tur.goto(position)
        self.snake.append(tur)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def move_snake(self):
        for tur_num in range(len(self.snake) - 1, 0, -1):  # to move t3 to t2 and t2 to t1 and t1 forward
            new_x = self.snake[tur_num - 1].xcor()  # s - 1 is second to last turtle.
            new_y = self.snake[tur_num - 1].ycor()
            self.snake[tur_num].goto(new_x, new_y)
        self.head.forward(MOVE)  # moves the first t1 forward 20 paces.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
