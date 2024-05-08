from random import randint, choice
from turtle import Screen

from car import Car
from crossingturtle import CrossingTurtle

screen = Screen()
screen.setup(width=800, height=500)
screen.canvwidth = 800
screen.canvheight = 500
crossing_turtle = CrossingTurtle(screen)
curr_speed = 10
cars = []
for i in range(0, 10):
    cars.append(Car(curr_speed, screen))

screen.onkeypress(crossing_turtle.move_forward, "Up")
screen.listen()


def game_still_playing():
    return True


def move_cars():
    num_cars_to_move = randint(1, len(cars))
    while num_cars_to_move > 0:
        choice(cars).move_forward()
        num_cars_to_move -= 1


def check_collisions():
    for car in cars:
        if car.car.xcor() == crossing_turtle.turtle.xcor() and car.car.ycor() == crossing_turtle.turtle.ycor():
            return True
    return False


def check_turtle_crossed():
    return crossing_turtle.turtle.ycor() > screen.canvheight / 2


counter = 0
while game_still_playing:
    move_cars()
    if check_collisions():
        game_still_playing = False
    if check_turtle_crossed():
        crossing_turtle.reset()
        curr_speed += 100
    counter += 1
    if counter % 5 == 0:
        cars.append(Car(curr_speed, screen))

print(f"Game Over, your score was {curr_speed / 100}")

screen.exitonclick()
