import numpy as np

arr = np.random.randint(1, 101, size=20)

maxima = np.max(arr)
minima = np.min(arr)

print("Array: ", arr)
print("Maximum value:", maxima)
print("Minimum value:", minima)