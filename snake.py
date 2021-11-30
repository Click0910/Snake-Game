from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snakes()

    def create_snakes(self):
        for snakes_position in POSITIONS:
            self.position_snake(snakes_position)

    def position_snake(self, snakes_position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(snakes_position)
        self.snakes.append(snake)

    def add_new_snake(self):
        self.position_snake(self.snakes[-1].position())

    def snake_movement(self):
        for snake_segment in range((len(self.snakes) - 1), 0, - 1):
            x_position = self.snakes[snake_segment - 1].xcor()
            y_position = self.snakes[snake_segment - 1].ycor()
            self.snakes[snake_segment].goto(x_position, y_position)

        self.snakes[0].forward(20)

    def reset_snake(self):
        for snake in self.snakes:
            snake.goto(1200, 1200)

        self.snakes.clear()
        self.create_snakes()

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)
