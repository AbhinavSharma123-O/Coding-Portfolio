import numpy as np
from scipy import linalg
A = np.array([[4, 2],
              [1, 3]])
print(f"Matrix A:\n{A}")
det_A = linalg.det(A)
print(f"Determinant of the matrix = {det_A}")
