import numpy as np
arr_arange = np.arange(1, 10, 2)
print(f"Using arange(): {arr_arange}")
arr_zeros = np.zeros((2, 3))
print(f"Using zeros():\n{arr_zeros}")
arr_ones = np.ones((3, 2))
print(f"Using ones():\n{arr_ones}")
arr_random = np.random.rand(2, 2)
print(f"Using random():\n{arr_random}")
matrix_A = np.array([[1, 2], [3, 4]])
print(f"Matrix A:\n{matrix_A}")
identity = np.eye(3)
print(f"Identity Matrix:\n{identity}")
diagonal = np.diag([1, 2, 3])
print(f"Diagonal Matrix:\n{diagonal}")



