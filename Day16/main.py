"""
Day 16 - Object Oriented Programming

 - Represent a domain object as an object with a set of functions it owns
 - Create an instance of that object and then invoke functions and store state in the object\
  - What an object "has" vs what an object "does"

Construction of an object

car = Car()

pypi.org - open source place to search for python libraries
"""

# https://docs.python.org/3/library/turtle.html
# import turtle
#
# timmy = turtle.Turtle()
# timmy.shape('turtle')
# timmy.color('blue')
# my_screen = turtle.Screen()
# my_screen.exitonclick()

# import prettytable
#
# table = prettytable.PrettyTable()
# table.add_column("Name", ["Seth", "Lexie", "Alex"])
# print(table)

# Day 16 - Coffee Machine as OOP


class CoffeeMachine:
    def __init__(self):
        self._milk = 100
        self._coffee = 200
        self._cream = 300

    def print_report(self):
        print(f"Milk: {self._milk}")
        print(f"Coffee: {self._coffee}")
        print(f"Cream: {self._cream}")


coffee_machine = CoffeeMachine()
coffee_machine.print_report()