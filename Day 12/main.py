"""
Day 12 - Scope

Local Scope - Exists within functions
Global Scope - Available to all functions and properties

Namespace - the scope of a given variable, function, etc

No block scope in Python

To update a global variable, use the global keyword
 - global <variable>
 - highly discouraged to modify global scope

Global Constants
 - Naming convention is SCREAMING_SNAKE_CASE
"""

# Number Guessing Game - Pick a number between 1-100, based on user input, make it "hard" or "easy"

import random

random_num = random.randint(1, 100)
diff = input("Would you like to play easy or hard? ")
num_attempts = 10 if diff == "easy" else 5

while num_attempts > 0:
    guess = int(input(f"You have {num_attempts} attempts remaining, guess a number: "))
    if guess == random_num:
        break
    elif guess > random_num:
        print("Too high!")
    else:
        print("Too low!")
    num_attempts -= 1

if num_attempts > 0:
    print(f"You won, the number was {random_num}")
else:
    print(f"You lost, the number was {random_num}")

