class Ques1:
    def __init__(self, a):
        self.a = a

    def even_or_odd(self):
        if self.a % 2 == 0:
            return f"{self.a} is an even number"
        else:
            return f"{self.a} is an odd number"