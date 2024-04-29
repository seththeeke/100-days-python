"""
Day 15 - Pycharm Setup and Coffee Machine
"""

# Coffee Machine

resources = {
    "water": 300,
    "milk": 200,
    "coffee_beans": 100,
    "money": 0
}

options = {
    "espresso": {
        "water": 100,
        "coffee_beans": 10,
        "money": 1.50
    },
    "coffee": {
        "water": 100,
        "milk": 50,
        "coffee_beans": 5,
        "money": 2.50
    },
    "cappuccino": {
        "water": 100,
        "milk": 100,
        "coffee_beans": 15,
        "money": 3.50
    }
}

coins = {
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
    "dollar": 1
}

def print_report():
    print(str(resources))

def collect_money(choice):
    cost = options[choice]["money"]
    print(f"You're {choice} costs {cost} money.")
    collected = 0
    still_entering = True
    while still_entering:
        coin = input("Put in a coin or say done, nickel, dime, quarter, dollar: ")
        if coin == "done":
            resources["money"] = collected
            still_entering = False
        else:
            collected += coins[coin]
            print(f"You have entered {collected} money.")
    return collected


def dispense_drink(choice):
    drink = options[choice]
    for key in drink:
        resources[key] -= drink[key]


dispensing = True


while dispensing:
    choice = input("Would you like to order(coffee, cappuccino, or espresso?: ")
    if choice == "report":
        print_report()
    elif choice == "stop":
        dispensing = False
    else:
        money = collect_money(choice)
        if money >= options[choice]["money"]:
            dispense_drink(choice)
            print(f"Enjoy your beverage, here is your chance {money - options[choice]['money']}")
        else:
            print(f"Sorry you don't have enough money!, drink is {options[choice]['money']} and you provided {money}")