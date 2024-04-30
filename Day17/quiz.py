import random


class Quiz:
    def __init__(self, question_bank):
        self.correct = 0
        self.incorrect = 0
        self.question_bank = question_bank
        self.question_index = 0

    def has_next_question(self):
        return self.correct + self.incorrect != len(self.question_bank)

    def next_question(self):
        question = self.question_bank[self.question_index]
        answer = input(question.question)
        if answer == question.answer:
            print(f"Correct! {question.answer}")
            self.correct += 1
        else:
            print(f"Incorrect! {question.answer}")
            self.incorrect += 1
        self.question_index += 1

    def print_report(self):
        print(f"You're score is {self.correct}/{self.correct + self.incorrect}")