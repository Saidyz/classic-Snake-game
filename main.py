from turtle import  Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.right ,"Right")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")

game_is_on = True  
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

    # DEtect collision with food,

    if snake.squares[0].distance(food)< 20:
        food.refresh()
        snake.extend()
        score.update_score()
    
    # Detect collusion with the wall.
    if snake.squares[0].xcor() >290 or snake.squares[0].xcor() < -290 or snake.squares[0].ycor() > 290 or snake.squares[0].ycor() < -290 :
        game_is_on = False
        score.game_over()
    
    #detect collision with the tail.]
    for square in snake.squares[2:]:
        if snake.squares[0].distance(square) < 10:
            game_is_on = False
            score.game_over()






    



screen.exitonclick()
