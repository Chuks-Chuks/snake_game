from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.small_food()

    def small_food(self):
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        random_x_position = random.randint(-280, 280)
        random_y_position = random.randint(-280, 280)
        self.goto(random_x_position, random_y_position)

    def big_meal(self):
        self.color("blue")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        random_x_position = random.randint(-280, 280)
        random_y_position = random.randint(-280, 280)
        self.goto(random_x_position, random_y_position)
