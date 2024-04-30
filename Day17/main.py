"""
Day 17 - Creating custom classes

 - create a class via the class keyword followed by a ClassName, e.g. class Name:
 - keyword "pass" allows you to create a class/function with no implementation
 class Name:
    pass
 - You can add attributes to a Class arbitrarily by setting them outside the object, e.g. user.new_attribute = "something"
 - You can specify properties on the class and initialize them in the class so all objects have the same properties
 - Initialization is __init__(self) is the constructor
"""


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.followers = 0
#
#     def add_follower(self):
#         self.followers += 1
#
#
# user_1 = User("John", 25)
# user_1.add_follower()

# Day 17 - Quiz Game, ask the user T/F questions and then track the users scores

import question
import quiz


questions = []
for index in range(0, 5):
    questions.append(question.Question())

quiz_game = quiz.Quiz(questions)
while quiz_game.has_next_question():
    quiz_game.next_question()
    quiz_game.print_report()

print("Thank you for playing!")
quiz_game.print_report()