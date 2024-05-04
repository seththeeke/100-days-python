"""
Day 19 - Instances, State, and Higher Order Functions


"""
import turtle
# Etch a Sketch

from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()
# inc = 10
#
#
# def handle_up(timmy, inc):
#     timmy.forward(inc)
#
#
# def handle_down(timmy, inc):
#     timmy.back(inc)
#
#
# def handle_right(timmy, inc):
#     timmy.right(inc)
#
#
# def handle_left(timmy, inc):
#     timmy.left(inc)
#
#
# def etch_a_sketch():
#     screen.onkey(handle_up, "Up")
#     screen.onkey(handle_down, "Down")
#     screen.onkey(handle_right, "Right")
#     screen.onkey(handle_left, "Left")
#     screen.listen()
#
#
# etch_a_sketch()

import random


def setup_race():
    starting_x_position = 0
    y_start = 0
    number_turtles = 6
    colors = ["red", "orange", "yellow", "green", "blue", "violet"]
    turtles = []
    while number_turtles > 0:
        some_turtle = Turtle()
        some_turtle.color(colors[number_turtles - 1])
        some_turtle.speed(random.randint(1, 50))
        some_turtle.shape("turtle")
        some_turtle.teleport(starting_x_position, y_start)
        y_start += 30
        turtles.append(some_turtle)
        number_turtles -= 1
    return turtles


def race_continues(turtles):
    for some_turtle in turtles:
        if some_turtle.xcor() >= 150:
            return False
    return True


def move_turtles(turtles):
    num_movements = random.randint(1, len(turtles))
    while num_movements > 0:
        random.choice(turtles).forward(1)
        num_movements -= 1


def get_winner(turtles):
    for some_turtle in turtles:
        if some_turtle.xcor() >= 150:
            return some_turtle
    return {}

screen = Screen()
screen.setworldcoordinates(0, 0, 150, 150)
turtles = setup_race()
guess = input("Guess the winning color: ")
while race_continues(turtles):
    move_turtles(turtles)

winner = get_winner(turtles)
print(f"The winner was {str(winner.color())}")

# Must be last command
screen.exitonclick()