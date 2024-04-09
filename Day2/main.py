"""
Notes

# Primitive Data Types

Strings - Array of Characters
 - Can access characters in String by an index, Subscripting, e.g. "Hello"[0] = "H"
Integers - Whole numbers
 - 123
 - In python, you can use _ to make numbers more readible and the intepreter will ignore them, e.g. 123_345_567 = 123345567
Floats - Numbers with decimal precision
Boolean - True or False values

# Functions
 - Using the type function will return the entities data type, e.g. type(123)
 - Using the str function, it will cast the entity to a String, e.g. str(123)
 - Using the float function, it will cast the entity to a Float
 - Using the round function, you can specify the precision of the given rounding, e.g. round(2.66666, 2) = 2.66

# Mathematical Operations
 - All Basic Operations - +, -, *, /
 - All division operations will return a Float
 - Exponents are **, e.g. 2**3 = 8
 - Floor division is //, e.g. 8//3 = 2
 - Shorthand is same as Java, +=, -=, etc.

# f-String
 - Allows you to add bracketed templating into a string
 - f"Your score is {score} and the team that won was {this_team}"
"""

# Two Digit String Sample Problem
# two_digit_string = input("Enter a two digit number")
# print(float(two_digit_string[0]) + float(two_digit_string[1]))

# BMI Calculator
# weight = float(input("Enter a weight in lbs"))
# height = float(input("Enter a height in meters"))
# bmi = int(weight/height**2)
# print(bmi)

# Weeks Remaining Calculator
# age = int(input("Enter your age"))
# weeks_remaining = 4000 - (age*52)
# print(f"You have {weeks_remaining} weeks left in your life")

# Day 2 Project - Tip Calculator - Given a total bill, the desired tip percentage, and the number of people,
# output the total amount each person pays
bill_amount = float(input("What is the bill amount? "))
desired_tip_percentage = float(input("What is the desired tip percentage? "))
people_split = int(input("How many people do you want to split the bill? "))

tip_amount = bill_amount * (desired_tip_percentage/100)
total_bill = bill_amount + tip_amount
amount_per_person = round(total_bill / people_split, 2)
print(f"Your final amount per person is ${amount_per_person}")
