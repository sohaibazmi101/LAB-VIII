import numpy as np

class Ques3:
    def __init__(self):
        self.arr = np.arange(1,100)

    def display_prime(self):
        print("Prime numbers between 1 and 100:")
        for num in self.arr:
            if num > 1:
                for i in range(2, int(num**0.5) + 1):
                    if (num % i) == 0:
                        break
                else:
                    print(num, end=' ')
        print()