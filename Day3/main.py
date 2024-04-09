"""
Control Flow and Logical Operators

if condition:
  do something
elif condition:
  do something else
else:
  do something else

Conditionals
 - >, <, >=, <=, ==, !=

Logical Operators
 -
"""

# Odd or Even
# num = int(input("Enter a number: \n"))
# if (num % 2) == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

# BMI with Description
# weight = float(input("Enter a weight in lbs"))
# height = float(input("Enter a height in meters"))
# bmi = int(weight/height**2)
# if bmi > 35:
#     print("You are extremely obese")
# elif bmi > 30:
#     print("You are obese")
# elif bmi > 25:
#     print("You are overweight")
# elif bmi > 18:
#     print("You are normal")
# else:
#     print("You are underweight")

# Build a program which determines if a given year is a leap year
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Python Pizza
# print("Thanks for choosing pizza")
# size = input("Enter the size of pizza, S, M, or L: ")
# add_pepperoni = input("Would you like to add pepperoni? Y/N: ")
# extra_cheese = input("Would you like to add extra cheese? Y/N: ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your bill is ${bill}")

# Love Calculator - Buzzfeed Article Algorithm
# print("Welcome to the love calculator")
# name1 = input("What is your name? ").upper()
# name2 = input("What is their name? ").upper()
#
# numT = name1.count("T") + name2.count("T")
# numR = name1.count("R") + name2.count("R")
# numU = name1.count("U") + name2.count("U")
# numE = name1.count("E") + name2.count("E")
# numL = name1.count("L") + name2.count("L")
# numO = name1.count("O") + name2.count("O")
# numV = name1.count("V") + name2.count("V")
#
# trueTotal = numT + numR + numU + numE
# loveTotal = numL + numO + numV + numE
#
# print(f"You score is: {trueTotal}{loveTotal}")

# Treasure Island Adventure Game
print("Welcome to Treasure Island!")
decision = input("You are at a cross road, do you want to go left or right, R/L: ")
if decision == "R":
    print("Game over, you died because of a tiger")
else:
    decision = input("You are at a river, swim across or wait for a boat, S/B: ")
    if decision == "S":
        print("Game over, you were eaten by an alligator")
    else:
        decision = input("You have gotten across the river and are presented with 3 doors, Yellow, Red, or Blue, "
                         "which do you choose, Y, R, B: ")
        if decision == "Y":
            print("You won the game!")
        else:
            print("Game over, you chose poorly")
