class Scoreboard:
    def __init__(self):
        self.left = 0
        self.right = 0

    def reset(self):
        self.left = 0
        self.right = 0

    def inc_left(self):
        self.left += 1

    def inc_right(self):
        self.right += 1

    def write_score(self):
        pass
