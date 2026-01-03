import numpy as np
data = [1, 2, 3, 4, 5, 6, 7, 8]
arr1D = np.array(data)
print(f"1D Array:{arr1D}")
print(f"Shape: {arr1D.shape}")
arr2D = arr1D.reshape(2, 4)
print(f"2D Matrix (2x4):{arr2D}")
print(f"Shape: {arr2D.shape}")
arr3D = arr1D.reshape(2, 2, 2)
print(f"3D Matrix (2x2x2):{arr3D}")
print(f"Shape: {arr3D.shape}")
