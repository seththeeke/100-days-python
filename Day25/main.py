"""
Day 25 - Reading files from CSV w/Pandas
"""

# with open("weather_data.csv") as file:
#     csv_data = file.readlines()

# import csv
#
# with open("weather_data.csv") as file:
#     csv_data = csv.reader(file)
#     for row in csv_data:
#         print(row)

# https://pandas.pydata.org/
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# # Pandas CSV Data is Broken into Series and Data Frames
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# # Pandas has a number of built in data analysis functions
# print(data["temp"].mean())
#
# #  You can fetch rows, columns by a condition
# print(data[data.day == "Monday"])
#
# # Create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [20, 30, 40]
# }
# to_pandas = pandas.DataFrame(data_dict)
# to_pandas.to_csv("data.csv")

# 50 States Guessing Game - Allow a user to guess as many states as possible and visualize them on the map
from turtle import Screen, Turtle

screen = Screen()
screen.bgpic("blank_states_img.gif")
t = Turtle()
t.penup()
t.hideturtle()
state_data = pandas.read_csv("50_states.csv")
print(state_data)
wrong_answers = 0
correct_answers = 0
while wrong_answers < 3:
    answer = screen.textinput("State Guessing Game", "Guess a State")
    df_answer = state_data[state_data.state == answer]
    if df_answer.empty:
        wrong_answers += 1
    else:
        correct_answers += 1
        t.teleport(float(df_answer.x), float(df_answer.y))
        t.write(answer)

print(f"You got {correct_answers} out of 50 states")
screen.exitonclick()