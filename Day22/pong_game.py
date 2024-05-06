from turtle import Screen

from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor('black')
        self.left_paddle = Paddle()
        self.right_paddle = Paddle()
        self.scoreboard = Scoreboard()
        self.ball = Ball()

    def start_new_game(self):
        self.initialize_board()
        while self.game_still_playing():
            self.ball.move()
            if self.ball_collided():
                # update ball direction
                pass
            if self.ball_out_of_play():
                # update score
                # reset paddles and new ball
                pass

    def initialize_board(self):
        # Draw dotted line in center
        # reset scoreboard
        # reset paddles and new ball
        pass

    def ball_out_of_play(self):
        # check if ball has left the field of play
        pass

    def game_still_playing(self):
        return self.scoreboard.left < 10 and self.scoreboard.right < 10

    def ball_collided(self):
        pass
