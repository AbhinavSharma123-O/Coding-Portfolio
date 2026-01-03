import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(f"Array:{arr}")
print(f"Number of dimensions (ndim): {arr.ndim}")
print(f"Shape of array (shape): {arr.shape}")
print(f"Total number of elements (size): {arr.size}")
print(f"Sum of all elements: {arr.sum()}")
print(f"Mean of all elements: {arr.mean()}")
sorted_arr = np.sort(arr)
print(f"Sorted array:{sorted_arr}")
print(f"Sine of array elements:{np.sin(arr)}")
