from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard

snake = Snake()
screen = Screen()
food = Food()
score = ScoreBoard()

screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.count()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for t in snake.turtles[1:]:
        if snake.head.distance(t) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
