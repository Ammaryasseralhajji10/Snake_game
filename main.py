from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)
snake1 = Snake()
food1 = Food()
score1 = Scoreboard()

screen.listen()
game_is_on = True

screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.right, "Right")
screen.onkey(snake1.left, "Left")


while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake1.move()
    if snake1.head.distance(food1) < 15:
        food1.refresh() 
        score1.collision()
        snake1.extend()
    if snake1.head.xcor() > 290 or snake1.head.xcor() < -290 or snake1.head.ycor() > 290 or snake1.head.ycor() < -290:
        score1.heigh_score()
        snake1.reset_snake()
        # score1.collision_with_wall()
        # game_is_on = False

    #detect collision with tails
    #if head colides with any segment in tails
        #trigger game_over
    for segment in snake1.all_squares[1:-1]:
        if snake1.head.distance(segment) < 10:
            score1.heigh_score()
            snake1.reset_snake()
            # game_is_on = False
            # score1.collision_with_wall()

        



screen.exitonclick()