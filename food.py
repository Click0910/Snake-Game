from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.pos_food()

    def pos_food(self):
        x_position_food = random.randint(-330, 330)
        y_position_food = random.randint(-330, 330)
        self.goto(x_position_food, y_position_food)




