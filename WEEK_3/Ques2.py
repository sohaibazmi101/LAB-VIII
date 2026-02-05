class Ques2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def largest(self):
        if self.a >= self.b and self.a >= self.c:
            return f"{self.a} is the largest number"
        elif self.b >= self.a and self.b >= self.c:
            return f"{self.b} is the largest number"
        else:
            return f"{self.c} is the largest number"