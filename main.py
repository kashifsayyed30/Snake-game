import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()  # creating a new screen that will show the window
screen.setup(width=600, height=600)  # size of screen
screen.bgcolor("dark blue")  # setting the screens background color to black
screen.title("Snake Game")  # sets title for screen
screen.tracer(0)  # turns animation off on screen

s1 = Snake()
food = Food()
score = Scoreboard()

screen.listen()  # listener for screen
screen.onkey(s1.up, "Up")
screen.onkey(s1.down, "Down")
screen.onkey(s1.left, "Left")
screen.onkey(s1.right, "Right")

game_started = True

while game_started:
    screen.update()  # refresh screen and re draw animation
    time.sleep(0.1)  # sleep by 1 sec. Adds 1 sec delay after each turtle moves
    s1.move_snake()

    # detect food collision
    if s1.head.distance(food) < 15:
        food.refresh_food()
        s1.extend()
        score.increase_score()
    # detect collision with wall
    if s1.head.xcor() > 290 or s1.head.xcor() < -290 or s1.head.ycor() > 290 or s1.head.ycor() < -290:
        game_started = False
        score.game_over()
    # detect collision with tail
    for segment in s1.snake[1:]:
        if s1.head.distance(segment) < 10:
            game_started = False
            score.game_over()



screen.exitonclick()  # removes the screen from display when users clicks on it.
