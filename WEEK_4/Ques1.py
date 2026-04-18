class Ques1:
    def __init__(self):
        self.numbers = [10, 20, 30, 40, 50]

    def sum(self):
        total = sum(self.numbers)
        return total
    def average(self):
        avg = sum(self.numbers) / len(self.numbers)
        return avg