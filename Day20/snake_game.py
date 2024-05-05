from random import randint
from turtle import Turtle


class SnakeGame:
    def __init__(self, snake, screen):
        self.snake = snake
        self.screen = screen
        self.dot = {}

    def start(self):
        self.screen.onkey(self.change_direction_up, "Up")
        self.screen.onkey(self.change_direction_down, "Down")
        self.screen.onkey(self.change_direction_right, "Right")
        self.screen.onkey(self.change_direction_left, "Left")
        self.screen.listen()
        self.snake.initialize_snake()
        self.dot = self.add_dot()
        while self.still_playing():
            self.snake.move_snake()
            print(f"Snake X: {self.snake.xcor} - Snake Y: {self.snake.ycor}")
            print(f"Dot X: {self.dot.xcor()} - Dot Y: {self.dot.ycor()}")
            if self.has_eaten_dot():
                self.dot.color("black")
                self.snake.add_segment()
                self.dot = self.add_dot()

    def add_dot(self):
        rand_x = int(randint(-300, 300)/20) * 20
        rand_y = int(randint(-300, 300)/20) * 20
        dot = Turtle(shape="square")
        dot.color("white")
        dot.penup()
        dot.teleport(rand_x, rand_y)
        return dot

    def change_direction_up(self):
        self.snake.direction = "U"

    def change_direction_down(self):
        self.snake.direction = "D"

    def change_direction_left(self):
        self.snake.direction = "L"

    def change_direction_right(self):
        self.snake.direction = "R"

    def has_eaten_dot(self):
        return self.snake.xcor == self.dot.xcor() and self.snake.ycor == self.dot.ycor()

    def still_playing(self):
        return True
