from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title("Snake_Game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
score = ScoreBoard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on == True:
    screen.update()
    time.sleep(0.1)

    snake.snake_movement()

    #Collision with food
    if snake.snakes[0].distance(food) < 15:
        food.pos_food()
        snake.add_new_snake()
        score.increase_score()

    #Collision with wall
    if snake.snakes[0].xcor() > 340 or snake.snakes[0].xcor() < -340 or snake.snakes[0].ycor() > 340 or  \
            snake.snakes[0].ycor() < -340:
        score.reset_game()
        snake.reset_snake()

    #Collision With tail
    for part_snake in snake.snakes[1:]:
        if snake.snakes[0].distance(part_snake) < 10:
            score.reset_game()
            snake.reset_snake()


screen.exitonclick()
