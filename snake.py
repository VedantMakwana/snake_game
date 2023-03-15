from turtle import Turtle
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake():

    def __init__(self):
        self.turtles = []
        self.creat_snake()
        self.head = self.turtles[0]

    def creat_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def move(self):
        for t in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[t - 1].xcor()
            y = self.turtles[t - 1].ycor()
            self.turtles[t].goto(x, y)
        self.head.fd(20)

    def add_segment(self,position):
        new_turtle = Turtle("square")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def reset(self):
        for i in self.turtles:
            i.goto(1500,1500)
        self.turtles.clear()

        self.creat_snake()
        self.head = self.turtles[0]

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





