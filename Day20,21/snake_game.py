from random import randint
from turtle import Turtle


class SnakeGame:
    def __init__(self, snake, screen):
        self.snake = snake
        self.screen = screen
        self.dot = {}

    def start(self):
        self.draw_border()
        self.screen.onkey(self.change_direction_up, "Up")
        self.screen.onkey(self.change_direction_down, "Down")
        self.screen.onkey(self.change_direction_right, "Right")
        self.screen.onkey(self.change_direction_left, "Left")
        self.screen.listen()
        self.snake.initialize_snake()
        self.dot = self.add_dot()
        still_playing = True
        while still_playing:
            self.snake.move_snake()
            if self.is_out_of_bounds() or self.snake.is_collided_with_self():
                still_playing = False
            else:
                if self.has_eaten_dot():
                    self.dot.color("black")
                    self.snake.add_segment()
                    self.dot = self.add_dot()
        print(f"Game Over, you scored {self.snake.get_length()} points")

    def add_dot(self):
        rand_x = int(randint(-300, 300)/20) * 20
        rand_y = int(randint(-300, 300)/20) * 20
        dot = Turtle(shape="square")
        dot.color("white")
        dot.penup()
        dot.teleport(rand_x, rand_y)
        return dot

    def change_direction_up(self):
        if self.snake.direction != "D":
            self.snake.direction = "U"

    def change_direction_down(self):
        if self.snake.direction != "U":
            self.snake.direction = "D"

    def change_direction_left(self):
        if self.snake.direction != "R":
            self.snake.direction = "L"

    def change_direction_right(self):
        if self.snake.direction != "L":
            self.snake.direction = "R"

    def has_eaten_dot(self):
        return self.snake.xcor == self.dot.xcor() and self.snake.ycor == self.dot.ycor()

    def is_out_of_bounds(self):
        return self.snake.xcor > 300 or self.snake.xcor < -300 or self.snake.ycor > 300 or self.snake.ycor < -300

    def draw_border(self):
        border_turtle = Turtle(shape="square")
        border_turtle.color("white")
        border_turtle.teleport(-320, 320)
        border_turtle.forward(600)
        border_turtle.right(90)
        border_turtle.forward(600)
        border_turtle.right(90)
        border_turtle.forward(600)
        border_turtle.right(90)
        border_turtle.forward(600)
