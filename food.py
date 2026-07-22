from turtle import Turtle
import random as rnd

COLOR = "red"
X_MAX = 280
Y_MAX = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = rnd.randint(-X_MAX, X_MAX)
        y = rnd.randint(-Y_MAX, Y_MAX)
        self.goto(x, y)