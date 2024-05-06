from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.direction = "L"
        self.xcor = 0
        self.ycor = 0
        pass

    def initialize_snake(self):
        for i in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(i * 20, 0)
            segment.xcor()
            segment.speed(1)
            self.snake_segments.append(segment)

    def move_snake(self):
        index = len(self.snake_segments) - 1
        while index >= 1:
            segment = self.snake_segments[index]
            seg_front = self.snake_segments[index - 1]
            segment.teleport(seg_front.xcor(), seg_front.ycor())
            index -= 1
        front_segment = self.snake_segments[0]
        if self.direction == "L":
            front_segment.teleport(front_segment.xcor() - 20, front_segment.ycor())
        elif self.direction == "R":
            front_segment.teleport(front_segment.xcor() + 20, front_segment.ycor())
        elif self.direction == "U":
            front_segment.teleport(front_segment.xcor(), front_segment.ycor() + 20)
        else:
            front_segment.teleport(front_segment.xcor(), front_segment.ycor() - 20)
        self.xcor = front_segment.xcor()
        self.ycor = front_segment.ycor()

    def add_segment(self):
        back_segment = self.snake_segments[-1]
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed(1)
        segment.teleport(back_segment.xcor() + 20, back_segment.xcor())
        self.snake_segments.append(segment)

    def is_collided_with_self(self):
        for index in range(1, len(self.snake_segments) - 1):
            if self.snake_segments[index].xcor() == self.xcor and self.snake_segments[index].ycor() == self.ycor:
                return True
        return False

    def get_length(self):
        return len(self.snake_segments) - 3
