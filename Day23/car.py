from turtle import Turtle
from random import randint, choice


class Car:
    def __init__(self, speed, screen):
        self.car = Turtle()
        self.speed = speed
        self.car.speed(speed)
        self.car.shape("square")
        self.car.color(choice(["blue", "yellow", "red", "purple"]))
        self.car.penup()
        self.car.teleport(int(screen.canvwidth/2), randint(int(screen.canvheight/2 - 50) * -1, int(screen.canvheight/2 - 50)))
        self.car.left(180)

    def move_forward(self):
        self.car.forward(10)
