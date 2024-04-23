"""
Day 14 - Higher or Lower

Create a game comparing instagram followers between two people

"""

import random


def gen_random_dataset(max_value):
    data = {}
    for i in range(max_value):
        data["name" + str(i)] = random.randint(1, 100000)
    return data


print("Welcome to higher or lower!")

game_data = gen_random_dataset(100)
correct_answer = True
num_correct = 0
while correct_answer:
    rand_a = random.choice(list(game_data.keys()))
    rand_b = random.choice(list(game_data.keys()))
    guess = input(f"Who has more followers? A: {rand_a} or B: {rand_b}: ")
    if guess == "A":
        correct_answer = game_data[rand_a] > game_data[rand_b]
    else:
        correct_answer = game_data[rand_b] > game_data[rand_a]
    if correct_answer:
        print("Correct! Keep Going!")
        num_correct += 1
    print(f"The number of followers were {rand_a}: {game_data[rand_a]} and {rand_b}: {game_data[rand_b]}")

print(f"Game over, you got {num_correct} correct answers.")
