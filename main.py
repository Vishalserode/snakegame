from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
food = Food()
scoreboard = ScoreBoard()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.add_big()
        food.refresh()
        scoreboard.score_reset()

    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <  -280:
        is_on = False
        scoreboard.game_over()

    for segm in snake.segment[1:]:
        if snake.head.distance(segm) < 10:
            is_on = False
            scoreboard.game_over()
        


screen.exitonclick()