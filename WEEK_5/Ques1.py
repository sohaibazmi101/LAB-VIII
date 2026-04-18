import numpy as np

class Ques1:
    def __init__(self):
        self.arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def display(self):
        print("Original Array:")
        print(self.arr)
        print("Shape of the Array:", self.arr.shape)
        print("Size of the Array:", self.arr.size)
        print("Data Type of the Array:", self.arr.dtype)