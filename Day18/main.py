from turtle import Turtle, Screen

import tkinter
from random import choice

timmy = Turtle()
timmy.shape("turtle")

screen = Screen()
screen.canvwidth = 1000
screen.canvheight = 1000

colors = ["red", "orange", "yellow", "green", "blue", "violet"]


def draw_square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)


def draw_dotted_line(length):
    distance = 0
    while distance < length:
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        distance += 20


def draw_shape_with_sides(num_sides):
    turn_inc = 360/num_sides
    sides_drawn = 0
    while sides_drawn < num_sides:
        timmy.forward(100)
        timmy.right(turn_inc)
        sides_drawn += 1


def draw_spirograph(num_circles):
    circles_drawn = 0
    turn_inc = 360/num_circles
    while circles_drawn < num_circles:
        timmy.color(choice(colors))
        timmy.circle(100)
        timmy.left(turn_inc)
        circles_drawn += 1

# draw_square()
# draw_dotted_line(500)
# for i in range(3, 30):
#     draw_shape_with_sides(i)

draw_spirograph(30)

screen.exitonclick()