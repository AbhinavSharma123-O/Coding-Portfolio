import numpy as np
from scipy import linalg
A = np.array([[4, 2],[1, 3]])
print("Matrix A:{A}")
eigenvalues, eigenvectors = linalg.eig(A)
print(f"Eigenvalues of the matrix:{eigenvalues}")
print(f"Eigenvectors of the matrix:{eigenvectors}")
