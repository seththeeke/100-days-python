import random

class Question:
    def __init__(self):
        self.question = "Is it True or False?"
        self.answer = random.choice(["True", "False"])

