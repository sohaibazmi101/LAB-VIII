import numpy as np

arr = np.random.randint(1, 101, size=20)

arr1 = np.reshape(arr, (4, 5))
print("ReshapedArray (4,5):\n", arr1)
arr2 = np.reshape(arr, (5, 4))
print("Reshaped Array (5,4):\n", arr2)