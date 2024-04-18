"""
Day 11 - Capstone Project Blackjack

Create a game of blackjack that has a dealer and a player and allows for hit or pass and then dealer to attempt to beat the player
"""

import random

print("Welcome to Blackjack!")
available_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


def get_score(cards):
    score = 0
    aces = 0
    for card in cards:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card != 'A':
            score += card
        else:
            aces += 1
    if score + 11 + aces - 1 < 21:
        score += 11 + aces - 1
    else:
        score += aces
    return score


def play_out_dealer(dealer_cards, player_score):
    dealer_score = get_score(dealer_cards)
    while dealer_score <= player_score:
        dealer_cards.append(random.choice(available_cards))
        print("Dealer hits and has cards " + str(dealer_cards))
        dealer_score = get_score(dealer_cards)
    return [dealer_score, dealer_cards]


player_cards = [random.choice(available_cards), random.choice(available_cards)]
player_score = get_score(player_cards)
dealer_cards = [random.choice(available_cards), random.choice(available_cards)]

print("Your cards are " + str(player_cards))
print("Dealer cards are " + str(dealer_cards[1]))
playing = True
while playing:
    hit = input("Do you want to hit or stand? ") == "hit"
    if hit:
        player_cards.append(random.choice(available_cards))
        print("Your cards are " + str(player_cards))
        player_score = get_score(player_cards)
        if player_score > 21:
            playing = False
    else:
        playing = False

if player_score > 21:
    print("You bust and lose!")
else:
    print("You scored " + str(player_score))
    dealer_final = play_out_dealer(dealer_cards, player_score)
    print("Final dealer cards are " + str(dealer_cards))
    if 21 >= dealer_final[0] > player_score:
        print("Dealer wins! Dealer Score: " + str(dealer_final[0] ))
    else:
        print("Dealer loses! Dealer Score: " + str(dealer_final[0] ))
