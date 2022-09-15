from turtle import Turtle
# import time
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.score = 0
        self.small_food()

    def refresh(self):
        random_x_position = random.randint(-280, 280)
        random_y_position = random.randint(-280, 280)
        self.goto(random_x_position, random_y_position)

    def small_food(self):
        self.score = 1
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def big_food(self):
        self.score = 5
        self.color("blue")
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.refresh()
