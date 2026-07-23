from turtle import Turtle, Screen

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MAX_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
s = Screen()

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.color_choice = s.textinput("Snake Color", prompt="Choose the color of the snake")
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create snake when u initialize the Object
    def create_snake(self):
        for position in INITIAL_POSITION:
            self.add_segment(position)

    # General function for the function of 'create_snake' & 'extend_snake'
    def add_segment(self, pos):
        snake = Turtle("square")
        snake.penup()
        snake.color(self.color_choice)
        snake.goto(pos)
        self.segments.append(snake)

    # Add a segment when the snake eat the food
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    # for seg_n in range(start = len(segments) - 1, stop = 0, step= -1):
    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_n].goto(self.segments[seg_n - 1].pos())
        self.head.fd(MAX_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
