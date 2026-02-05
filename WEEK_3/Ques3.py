class Ques3:
    def __init__(self, n):
        self.n = n
    def fibonacci(self):
        fib_sequence = []
        a, b = 0, 1
        for _ in range(self.n):
            fib_sequence.append(a)
            c = a + b
            a = b
            b = c
        return fib_sequence