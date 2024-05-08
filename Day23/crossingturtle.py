import turtle


class CrossingTurtle():
    def __init__(self, screen):
        self.turtle = turtle.Turtle()
        self.screen = screen
        self.turtle.shape('turtle')
        self.turtle.penup()
        self.turtle.teleport(0, screen.canvheight/2 * -1)
        self.turtle.left(90)
        pass

    def move_forward(self):
        self.turtle.forward(10)

    def reset(self):
        self.turtle.teleport(0, self.screen.canvheight / 2 * -1)
