"""
Day 4 - Randomisation and Lists

askpython.com allows you to search for python functionality

A module exists called random which allows for generation of random numbers

import random

random_int = random.randint(1, 100)
print(random_int)

Modules
 - A python module is a way of breaking up libraries in python that can be imported by their users
 - A module is as simple as a separate file

import my_module

print(my_module.pi)

random() will return a float between 0 and 1
to get a random float between X and Y, you would multiple the random float by the value of the maximum + the minimum

Lists
 - list = [item1, item2]
 - In python, lists can contain items of multiple data types
 - reference items in the list by index, e.g. list[0]
 - Can update items in the list by index as well, e.g. list[0] = new_item
 - Add item to the end of the list by using the append function, e.g. list.append(item)
 - Add multiple items by using the extend function, e.g. list.extend([item1, item2])
 - Will receive an IndexOutOfBounds if you end up referencing an index that does not exist
 - Can reference an item by a negative index which will search from the back of the list
"""

# Heads or Tails
# import random
#
# coin = random.randint(1, 2)
# if (coin == 1):
#     print("Heads!")
# else:
#     print("Tails!")

# Who Pays the Bill
# import random
#
# names_string = input("Enter a list of names separated by a comma: ")
# names = names_string.split(", ")
# random_index = random.randint(0, len(names) - 1)
# print(f"{names[random_index]} pays the bill!")

# Treasure Map
# line1 = [" ", " ", " "]
# line2 = [" ", " ", " "]
# line3 = [" ", " ", " "]
# map = [line1, line2, line3]
#
# location = input("Enter a location A-C, 1-3: ")
# col = location[0].upper()
# row = int(location[1]) - 1
#
# if col == "A":
#     col = 0
# elif col == "B":
#     col = 1
# else:
#     col = 2
#
# map[row][col] = "X"
#
# print(map)

# Day 4 Project - Rock, Paper, Scissors

import random

print("Welcome to Rock, Paper Scissors")
choice = input("Enter Rock, Paper or Scissors, R, P, or S: ")
choices = ["R", "P", "S"]
choice_int = choices.index(choice)
cpu_choice = random.randint(0, 2)

print(f"CPU Choice: {choices[cpu_choice]}")

if cpu_choice == choice_int:
    print("Its a Draw!")
else:
    if choice_int == 0:
        if cpu_choice == 1:
            print("You Lose!")
        else:
            print("You Win!")

    if choice_int == 1:
        if cpu_choice == 0:
            print("You Win!")
        else:
            print("You Lose!")

    if choice_int == 2:
        if cpu_choice == 0:
            print("You Lose!")
        else:
            print("You Win!")

