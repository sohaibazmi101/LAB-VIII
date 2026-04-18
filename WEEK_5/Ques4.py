import numpy as np

class Ques4:
    def __init__(self):
        self.arr = np.array([10, 20, 30, 40, 50, 60, 70])

    def array_indexing(self):
        print("Original array:", self.arr)
        print("Elements at even indices:", self.arr[::2])
        print("Elements at odd indices:", self.arr[1::2])

        print("\nSlice from index 1 to 4:", self.arr[1:5])
        print("Slice from start to index 3:", self.arr[:4])
        print("Slice from index 3 to end:", self.arr[3:]) 
        print("Slice with step 2:", self.arr[::2])
        print("Reverse array:", self.arr[::-1]) 