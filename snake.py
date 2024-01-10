from turtle import Turtle
NEW_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP =90
DOWN =270
LEFT =180
RIGHT =0
class Snake:
    def __init__(self):

        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
    def create_snake(self):
        for new in NEW_POSITION:
            self.big(new)

    def big(self, new):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(new)
        self.segment.append(snake)

    def add_big(self):
        self.big(self.segment[-1].position())
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(0)
