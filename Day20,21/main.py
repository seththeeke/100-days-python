from turtle import Turtle, Screen
from snake_game import SnakeGame
from snake import Snake

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title("Welcome to the Snake Game")
snake = Snake()
snake_game = SnakeGame(snake, screen)
snake_game.start()

screen.exitonclick()