import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = t.Screen()
# setting up the screen for the game.
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("Philip's Snake Game")
# the tracer method is used to pause animations on the surface to enable smooth transitioning as the code runs.
# for the animations to work properly (because the screen is paused, duh!) we need to call the update() method.
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
is_game_on = False
game_level = screen.textinput("CHOOSE YOUR LEVEL", "Type easy or hard to choose your difficulty.")

if game_level:
    # This basically switches the game on as it needs an input to
    is_game_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
meal_count = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food. Remember snake.segments[0] is the head of the snake. Which has been turned
    # to an attribute in the snake class as 'self.head'.

    # Just discovered the big food distance has to be increased.
    if snake.head.distance(food) < 17:
        meal_count += 1
        if meal_count % 5 == 0:
            food.big_meal()
            score.big_meal()
        else:
            food.small_food()
            score.update_score()
        snake.add_segment()

    # if snake.head.distance(food) < 20:
    #     if meal_count % 5 == 0:
    #         food.big_meal()
    #         snake.add_segment()
    #         score.big_meal()

    # Detect collision with the wall
    # Trying to make this for hard play.
    if game_level == 'hard':
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            is_game_on = False
            score.game_over_update()

    # If I want the snake to come out from the other side of the screen and not getting lost then
    if game_level == 'easy':
        if snake.head.xcor() > 295 or snake.head.xcor() < -295:
            new_x = -1 * snake.head.xcor()
            snake.head.goto(new_x, snake.head.ycor())

        if snake.head.ycor() > 295 or snake.head.ycor() < -295:
            new_y = -1 * snake.head.ycor()
            snake.head.goto(snake.head.xcor(), new_y)

    # Detecting collision with the snake's tail using my code. IT WORKED!!!!
    # for number in range(1, len(snake.segments)-1, 1):
    #     if snake.head.distance(snake.segments[number]) < 10:
    #         is_game_on = False
    #         score.game_over_update()
    #
    # Detecting collision with the snake's tail using slicing. Totally effective. Just learned the concept.
    for snake_body in snake.segments[1:]:
        if snake.head.distance(snake_body) < 10:
            is_game_on = False
            score.game_over_update()
screen.exitonclick()
