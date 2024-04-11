"""
Day 5 - Loops

For loop
 - for item in list:

Range function
 - for number in range(a, b):
 - Creates a range between 2 sets of numbers
 - does not include b in the range
 - increases by one by default, can change the step size by adding an additional parameter, range(a, b, step)
"""

# Average Height of Students
# heights = input("Enter a list of heights: ")
# heights_list = heights.split(",")
# heightSum = 0
# for height in heights_list:
#     heightSum += int(height)
#
# print(f"The average height is {heightSum/len(heights_list)}")

# Highest Score
# scores = input("Enter list of scores: ")
# scores_list = scores.split(',')
# max_score = -1
# for score in scores_list:
#     int_score = int(score)
#     if int_score > max_score:
#         max_score = int_score
#
# print(f"The max score is {max_score}")

# Adding Even Numbers, Calculate sum from 0 to input of only even numbers
# range_max = int(input("Enter value to count to: "))
# total = 0
# for n in range(0, range_max + 1, 2):
#     total += n
#
# print(f"Sum of all even numbers to {range_max} is {total}")

# FizzBuzz
# numbers = input("Enter numbers separated by a comma: ").split(",")
# for num in numbers:
#     num_int = int(num)
#     if num_int % 3 == 0:
#         print("Fizz")
#     if num_int % 5 == 0:
#         print("Buzz")

# Day 5 Project - Password Generator
import random

num_letters = int(input("How many letters would you like: "))
num_symbols = int(input("How many symbols would you like: "))
num_numbers = int(input("How many numbers would you like: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['/', ',', '%', '*', '#', '(', ')']

total_password_length = num_letters + num_symbols + num_numbers
password = ""
available_options = ["letter", "symbol", "number"]
remaining_letters = num_letters
remaining_symbols = num_symbols
remaining_numbers = num_numbers
for index in range(0, total_password_length):
    option = available_options[random.randint(0, len(available_options) - 1)]
    if option == "letter":
        password += random.choice(letters)
        remaining_letters -= 1
        if remaining_letters == 0:
            available_options.remove("letter")
    elif option == "symbol":
        password += random.choice(symbols)
        remaining_symbols -= 1
        if remaining_symbols == 0:
            available_options.remove("symbol")
    else:
        password += random.choice(numbers)
        remaining_numbers -= 1
        if remaining_numbers == 0:
            available_options.remove("number")

print(f"Your final password is {password}")