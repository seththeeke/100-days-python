"""
Day 7 - Hangman

 - When the game starts, a random work is selected
 - Allow the user to enter guesses until they either get the word or fail
 - Display the status of their word and their prior guesses
 - Display the art of their current hangman status
"""

import random


def print_curr(word_array):
    str_to_print = ""
    for i in range(len(word_array)):
        str_to_print += word_array[i]
    print(str_to_print)


def curr_to_guess(word_array):
    str_guess = ""
    for i in range(len(word_array)):
        str_guess += word_array[i]
    return str_guess


words = ['hello', 'world', 'rose', 'flower', 'soccer', 'theatre', 'game', 'somethinge']
word_to_guess = random.choice(words)
curr_ans = []
for index in range(len(word_to_guess)):
    curr_ans.append("_")
wrong_count = 0
guesses = ""
while curr_to_guess(curr_ans) != word_to_guess:
    print_curr(curr_ans)
    guessed_letter = input(f'Guess a letter, current guesses have been {guesses} : ')
    guesses += ", " + guessed_letter
    try:
        letter_exists = word_to_guess.index(guessed_letter) != -1
    except ValueError:
        letter_exists = False

    if letter_exists:
        print("Correct! Keep going!")
        for index in range(0, len(word_to_guess)):
            if word_to_guess[index] == guessed_letter:
                curr_ans[index] = guessed_letter
    else:
        print("Incorrect")
        wrong_count += 1
        if wrong_count > 5:
            break

if wrong_count > 5:
    print(f"Game over, you lose, the word was {word_to_guess}")
else:
    print_curr(curr_ans)
    print("You win! Congrats")
